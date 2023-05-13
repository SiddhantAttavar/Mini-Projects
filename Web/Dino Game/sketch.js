function setup() {
	freq = windowWidth;
	createCanvas(windowWidth, windowHeight - 50);
	fill(255);
	noStroke();
	textSize(width / 10);
	textAlign(CENTER, CENTER);
}

cacti = [];
x = 0;
y = 0;
vx = 1;
vy = 0;
a = 0.1;
freq = 0;
maxCollisionDist = Math.sqrt(35**2 + 20**2) + 2;
score = 0;
gameOver = false;
minObstacleRange = 125;
randRange = 150;

function draw() {
	translate(-x, 0);
	background(0);
	fill(0, 0, 255);
	rect(x, height - 5, width, 5);
	for (i = 0; i < vx; i++) {
	rect(x + 50 + i * 30, 50, 20, 20);
	}
	fill(255);
	for (i = vx; i < 10; i++) {
	rect(x + 50 + i * 30, 50, 20, 20);
	}
	fill(0, 255, 0);
	rect(x + width - 50, 50, 20, 20);
	if (gameOver || checkCollisions()) {
	text('Game over!\nYour score is: ' + score, x + width / 2, height / 2);
	return;
	}
	if (y > 0) {
	vy = vy - a;
	}
	y = max(0, y + vy);
	text(score, x + width / 2, height / 2);
	fill(255);
	rect(x + 20, height - 25 - y, 20, 20);
	fill(255, 0, 0);
	if ((x + width - freq) < vx && (x + width - freq) >= 0) {
	cacti.push(freq);
	rand = floor(Math.random() * (randRange + 75 * vx));
	freq = freq + (minObstacleRange * vx) + rand;
	}
	if (cacti[0] < x) {
	cacti.shift();
	score = score + 1;
	}
	for (i = 0; i < cacti.length; i++) {
	cacti[i] = cacti[i] - 1;
	rect(cacti[i], height - 55, 20, 50);
	}
	x = x + vx;
}

function keyPressed() {
	if ((keyCode == UP_ARROW || key == ' ') && y < 5) {
	vy = 4.5;
	}
	else if (key == 'r') {
	cacti = [];
	score = 0;
	freq = x + width;
	}
	else if (!isNaN(key)) {
		vx = max(1,parseInt(key));
		cacti = [];
		score = 0;
		freq = x + width;
	}
}

function mousePressed() {
	if (mouseX >= width - 50 && mouseX <= width - 20 && mouseY >= 50 && mouseY <= 70) {
	cacti = [];
	score = 0;
	freq = x + width;
	}
	else if (mouseY >= 50 && mouseY <= 70) {
	vx = floor((mouseX - 50) / 30) + 1;
	cacti = [];
	score = 0;
	freq = x + width;
	}
	else if (y < 10) {
	vy = 4.5;
	}
}

function checkCollisions() {
	for (i = 0; i < cacti.length; i++) {
	dis = Math.sqrt(abs(25 - y)**2 + abs(cacti[i] - x)**2);
	if (dis < maxCollisionDist) {
		return true;
	} 
	}
	return false;
}function setup() {
	freq = windowWidth;
	createCanvas(windowWidth, windowHeight - 50);
	fill(255);
	noStroke();
	textSize(width / 10);
	textAlign(CENTER, CENTER);
}

cacti = [];
x = 0;
y = 0;
vx = 1;
vy = 0;
a = 0.1;
freq = 0;
maxCollisionDist = Math.sqrt(35**2 + 20**2) + 2;
score = 0;
gameOver = false;

function draw() {
	translate(-x, 0);
	background(0);
	fill(0, 0, 255);
	rect(x, height - 5, width, 5);
	for (i = 0; i < vx; i++) {
	rect(x + 50 + i * 30, 50, 20, 20);
	}
	fill(255);
	for (i = vx; i < 10; i++) {
	rect(x + 50 + i * 30, 50, 20, 20);
	}
	fill(0, 255, 0);
	rect(x + width - 50, 50, 20, 20);
	if (gameOver || checkCollisions()) {
	text('Game over!\nYour score is: ' + score, x + width / 2, height / 2);
	return;
	}
	if (y > 0) {
	vy = vy - a;
	}
	y = max(0, y + vy);
	text(score, x + width / 2, height / 2);
	fill(255);
	rect(x + 20, height - 25 - y, 20, 20);
	fill(255, 0, 0);
	if ((x + width - freq) < vx && (x + width - freq) >= 0) {
	cacti.push(freq);
	rand = floor(Math.random() * 75);
	freq = freq + (75 * vx) + rand;
	}
	if (cacti[0] < x) {
	cacti.shift();
	score = score + 1;
	}
	for (i = 0; i < cacti.length; i++) {
	cacti[i] = cacti[i] - 1;
	rect(cacti[i], height - 55, 20, 50);
	}
	x = x + vx;
}

function keyPressed() {
	if ((keyCode == UP_ARROW || key == ' ') && y < 5) {
	vy = 4.5;
	}
	else if (key == 'r') {
	restart();
	}
	else if (!isNaN(key)) {
		vx = max(1, parseInt(key));
		restart();
	}
}

function mousePressed() {
	if (mouseX >= width - 50 && mouseX <= width - 20 && mouseY >= 50 && mouseY <= 70) {
	restart();
	}
	else if (mouseY >= 50 && mouseY <= 70) {
	vx = floor((mouseX - 50) / 30) + 1;
	restart();
	}
	else if (y < 10) {
	vy = 4.5;
	}
}

function checkCollisions() {
	for (i = 0; i < cacti.length; i++) {
	dis = Math.sqrt(abs(25 - y)**2 + abs(cacti[i] - x)**2);
	if (dis < maxCollisionDist) {
		return true;
	} 
	}
	return false;
}

function restart() {
	cacti = [];
	score = 0;
	freq = x + width;
	y = 0;
	vy = 0;
}