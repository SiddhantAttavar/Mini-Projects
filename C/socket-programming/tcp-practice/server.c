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
	server_addr.sin_addr.s_addr = INADDR_ANY;
	server_addr.sin_port = htons(PORT);
	if (bind(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
		printf("Cannot bind\n");
		return 0;
	}

	listen(sockfd, 3);
	sockfd = accept(sockfd, (struct sockaddr *)&server_addr, &addr_size);

	char line[1024];
	recv(sockfd, line, 1024, 0);
	printf("%s", line);
}
