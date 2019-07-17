rwidth=200
rheight=70
ryvalue=0



def setup():
   size (1000,1000)
   background(255,255,255)
   fill(255,255,255)
   rect(0,ryvalue,rwidth,rheight)#box1
   fill(0,0,0)
   textSize(40)
   text("ERASER", 20, 50)
   fill(91,93,207)
   rect(200,ryvalue,rwidth,rheight)#box2
   fill(196,0,155)
   rect(400,ryvalue,rwidth,rheight)#box3
   fill(239, 250, 80)
   rect(600,ryvalue,rwidth,rheight)#box4
   fill(170, 242, 183)
   rect(800,ryvalue,rwidth,rheight)#box5
   
   noStroke()
   
def draw(): #Runs over and over 
   
    if mousePressed and mouseY>rheight+25:
        ellipse(mouseX,mouseY,50,50)#draw with pen
         
    if mouseX>rwidth and mouseX<400 and mouseY<rheight:#box2
        fill(91,93,207)
    elif mouseX>rwidth and mouseX <600 and mouseY<rheight:#box3
        fill(196,0,155)
    elif mouseX>rwidth and mouseX<800 and mouseY<rheight:#box4
        fill(239, 250, 80)
    elif mouseX>rwidth and mouseX<1000 and mouseY<rheight:#box5
        fill(170, 242, 183)
    elif mouseX>rwidth/2 and mouseX<200 and mouseY<rheight:#box1
        fill(255, 255, 255)

    if keyPressed and key=="s" or key=="S":
        saveFrame()
        
    
        
        
      
    

    
        

    
        





              
