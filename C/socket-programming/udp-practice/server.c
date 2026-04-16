#include <assert.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <stdio.h>

#define PDR 10
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
struct sockaddr_in server_addr, clientaddr;
packet data_pkt, ack_pkt;
socklen_t addr_size = sizeof(clientaddr);

void receive_packet() {
	assert(recvfrom(sockfd, &data_pkt, sizeof(data_pkt), 0, (struct sockaddr*) &clientaddr, &addr_size) >= 0);
}

int drop_packet() {
	if ((rand() % 100) < PDR) {
		printf("DROP DATA: Seq. No. %d of size %lu Bytes\n", data_pkt.seq_no, data_pkt.size);
		return 1;
	}

	printf("RCVD DATA: Seq. No %d of size %lu Bytes\n", data_pkt.seq_no, data_pkt.size);

	ack_pkt.size = 1;
	ack_pkt.seq_no = data_pkt.seq_no;
	sendto(sockfd, &ack_pkt, sizeof(ack_pkt), 0, (struct sockaddr*) &clientaddr, addr_size);
	printf("SENT ACK: for PKT with Seq. No. %d\n", ack_pkt.seq_no);
	return 0;
}

int main() {
	srand((uint) time(0));

	// Setup socket
	sockfd = socket(AF_INET, SOCK_DGRAM, 0);
	memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

	if (bind(sockfd, (struct sockaddr*) &server_addr, sizeof(server_addr)) == -1) {
		printf("Unsuccesful bind\n");
		return 0;
	}

	// Read file
	FILE *fptr = fopen("output.txt", "w");
	do {
		do {
			receive_packet();
		} while(drop_packet());
		fprintf(fptr, "%s", data_pkt.data);
		seq_no++;
	} while (!data_pkt.is_last);

	fclose(fptr);
}
