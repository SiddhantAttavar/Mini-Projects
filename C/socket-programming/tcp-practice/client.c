#include <string.h>
#include <netinet/in.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 8080

int sockfd;
struct sockaddr_in server_addr;
socklen_t addr_size = sizeof(server_addr);

int main() {
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(PORT);
	inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr);
	if (connect(sockfd, (struct sockaddr*) &server_addr, sizeof(server_addr)) == -1) {
		printf("Cannot connect\n");
		return 0;
	}

	char line[1024] = "Hello World!\n";
	send(sockfd, line, strlen(line), 0);
	printf("%s", line);
}
