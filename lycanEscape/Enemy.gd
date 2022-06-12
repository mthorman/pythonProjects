extends KinematicBody

var velocity = Vector3.ZERO
var speed = 3
var max_x = 20
var max_y = 20

func _physics_process(delta):
	if translation.x > max_x:
		speed *= -1
	
	if translation.x < -max_x:
		speed *= -1
		
		
	velocity.x = speed
	move_and_collide(velocity*delta)
	
