extends KinematicBody

var gravity = 10
var velocity = Vector2(0,0)

var speed = 32

func _process(delta):
	move_character()
	
func move_character():
	velocity.x = -speed
	velocity.y += gravity 

	velocity = move_and_slide(velocity, Vector2.UP)
