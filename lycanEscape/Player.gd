extends KinematicBody

var velocity = Vector3()

var speed = 6
var gravity = -.2
var rotate_speed = .025
var jump_speed = 3

var bulletMaster
var gunshot

func _ready():
	bulletMaster = preload("res://Bullet.tscn")
	gunshot = get_parent().get_node("Gunshot")
	

func _physics_process(delta):
	velocity.y += gravity 
	velocity.x =0
	velocity.z =0
	
	if Input.is_action_pressed("fwd"):
		velocity -= transform.basis.z
	if Input.is_action_pressed("back"):
		velocity += transform.basis.z
	if Input.is_action_pressed("left"):
		velocity -= transform.basis.x
	if Input.is_action_pressed("right"):
		velocity += transform.basis.x
	
	if Input.is_action_just_pressed("jump"):
		if is_on_floor():
			velocity.y = jump_speed
			
	if Input.is_action_just_pressed("fire"):
		gunshot.play()
		
		var bullet = bulletMaster.instance()
		owner.add_child(bullet)
		bullet.transform = $Head/Gun.global_transform
		bullet.velocity = -bullet.transform.basis.z*bullet.bullet_speed
		
	move_and_slide(velocity*speed, Vector3.UP)
	
func _unhandled_input(event):
	if event is InputEventMouseMotion:
		rotate_y(-rotate_speed*event.relative.x/10)
		$Head.rotate_x(-rotate_speed*event.relative.y/10)
	
	
