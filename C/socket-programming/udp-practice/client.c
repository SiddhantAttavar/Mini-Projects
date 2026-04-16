#include <string.h>
#include <netinet/in.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define TIMEOUT 2
#define PORT 8080

typedef struct {
	size_t size;
	int seq_no;
	int is_last;
	int type;
	char data[1024];
} packet;

int sockfd, seq_no;
struct sockaddr_in server_addr;
packet data_pkt, ack_pkt;
socklen_t addr_size = sizeof(server_addr);

void build_packet(char *line, int is_last) {
	data_pkt.size = strlen(line);
	data_pkt.seq_no = seq_no;
	data_pkt.type = 0;
	strcpy(data_pkt.data, line);
	data_pkt.is_last = is_last;
}

void send_packet() {
	sendto(sockfd, &data_pkt, sizeof(data_pkt), 0, (struct sockaddr*) &server_addr, addr_size);
	printf("SENT DATA: Seq. No %d of size %lu Bytes\n", data_pkt.seq_no, data_pkt.size);
}

int ack_recevied() {
	if (recvfrom(sockfd, &ack_pkt, sizeof(ack_pkt), 0, (struct sockaddr*) &server_addr, &addr_size) < 0) {
		printf("RESENT DATA: Seq. No %d of size %lu Bytes\n", data_pkt.seq_no, data_pkt.size);
		return 0;
	}
	printf("RCVD ACK: for PKT with Seq.No. %d\n", ack_pkt.seq_no);
	return 1;
}

int main() {
	// Read file
	FILE *fptr = fopen("input.txt", "r");
	char lines[1024][1024];
	int line_count;
	for (line_count = 0; line_count < 1024; line_count++) {
		if (!fgets(lines[line_count], 1024, fptr)) {
			break;
		}
	}
	fclose(fptr);

	// Print file
	printf("File (input.txt) contents:\n");
	for (int i = 0; i < line_count; i++) {
		printf("%s", lines[i]);
	}
	printf("\n");

	// Setup socket
	sockfd = socket(AF_INET, SOCK_DGRAM, 0);
	struct timeval tv;
	tv.tv_sec = TIMEOUT;
	tv.tv_usec = 0;
	setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));
	memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

	for (int i = 0; i < line_count; i++) {
		build_packet(lines[i], i == line_count - 1);
		do {
			send_packet();
		} while (!ack_recevied());
		seq_no++;
	}
}
