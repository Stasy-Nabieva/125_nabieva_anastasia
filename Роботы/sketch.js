function setup()
{
	//create a canvas for the robot
	createCanvas(1000, 700);
}

function draw()
{
	strokeWeight(2);

	//robot body 1 - delete this code and make your own robot body
	fill(200);
    fill(66,170,255)
	rect(90, 200, 120, 130); //body
    fill(255,228,196);
	rect(65, 200, 25, 150); //left hand
	rect(210, 200, 25, 150); //right hand
	
    fill(66,170,255)
    rect(65,200,25,80) //left sleeve
    rect(210, 200, 25, 80);//right sleeve
    fill(0,0,255)
    rect(90,330,120,20) //pants
    rect(90, 330, 30, 150); //left leg
	rect(180, 330, 30, 150); //right leg

	//robot body 2 - delete this code and make your own robot body
    fill(253,233,16)
	rect(390, 200, 120, 130,5); //body
	rect(370, 200, 20, 100,5);//left hand
	rect(510, 200, 20, 100,5);//right hand
	rect(390, 330, 20, 110,5);//left leg
	rect(490, 330, 20, 110,5);//right leg


	//robot body 3 - delete this code and make your own robot body
    fill(255,0,213)
	rect(690, 200, 120, 130);//body
	rect(690, 330, 30, 150);//left leg
	rect(780, 330, 30, 150);//right leg
    fill(255,188,217)
    rect(665, 200, 25, 150);//left hand
	rect(810, 200, 25, 150);//right hand
    fill(255,0,213)
    rect(665, 200, 25, 80);//left sleeve
	rect(810, 200, 25, 80);//right sleeve

	// !!! Draw the robot heads - You shouldn't need to change this code !!!

	//robot head 1
	fill(255,228,196);
    ellipse(150,150,90,60)
    noFill();
    rect(90,100,120,100)
    arc(150,150,100,40,120,90)
    //robot head 2
    fill(253,233,16)
	rect(400, 100, 100, 100, 10);
    //robot head 3
    fill(255,188,217)
	rect(700, 100, 100, 100, 10);
    

	//ears
    noFill();
	//robot ears 1
	rect(90, 70, 10, 30); //left
	rect(200, 70, 10, 30);//right

	//robot ears 2
    fill(253,233,16)
	ellipse(400, 130, 15, 40);
	ellipse(500, 130, 15, 40);

	//robot hears 3
    fill(253,131,233)
    ellipse(750,100,150,40)
	ellipse(690, 170, 40, 150);
	ellipse(810, 170, 40, 150);


	//robot 1's eyes
	fill(0);
    ellipse(125,140,5,5) //left eye
	ellipse(175,140,5,5) //right eye

	//robot 2's eyes
    fill(0)
	ellipse(425, 130, 26, 26);//left eye
	ellipse(475, 130, 26, 26); //right eye
	fill(255,255,255);
    ellipse(425, 130, 20, 20); //left eye
    ellipse(475, 130, 20, 20); //right eye

	//robot 3's eyes
    fill(0);
	ellipse(725, 140, 5, 5);
	ellipse(775, 140, 5, 5);


	//robots' noses
	fill(255, 0, 0);
    //robot 2 nose
	fill(0)
    ellipse(450,150,20,10)



	//robot 2 mouth
    noFill()
	beginShape();
	vertex(428, 175);
	vertex(436, 185);
	vertex(442, 175);
	vertex(450, 185);
	vertex(458, 175);
	vertex(466, 185);
	vertex(474, 175);
	endShape();

	//robot 3 mouth
    fill(0)
	ellipse(750,170,15,15)
}
