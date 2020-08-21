import turtle;
move_turtle = turtle.Turtle()
move_turtle.speed(2)

def octagon():
  # function to creating octagon
  move_turtle.forward(100)
  move_turtle.right(45);
  move_turtle.forward(100)
  move_turtle.right(45);
  move_turtle.forward(100)
  move_turtle.right(45);
  move_turtle.forward(100)
  move_turtle.right(45);
  move_turtle.forward(100)
  move_turtle.right(45);
  move_turtle.forward(100)
  move_turtle.right(45);
  move_turtle.forward(100)
  move_turtle.right(45);
  move_turtle.forward(100)

  
for i in range(5):
  octagon()