@namespace
class SpriteKind:
    portal = SpriteKind.create()
    portal2 = SpriteKind.create()
    heart = SpriteKind.create()
    MOGUS = SpriteKind.create()

def on_left_pressed():
    mySprite.set_image(assets.image("""
        myImage3
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_left_released():
    mySprite.set_image(assets.image("""
        LINK
    """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_on_overlap(sprite, otherSprite):
    mySprite2.destroy()
    info.change_score_by(50)
sprites.on_overlap(SpriteKind.player, SpriteKind.MOGUS, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    d.destroy()
    info.change_score_by(10)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    pause(1000)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

d: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
Render.toggle_view_mode()
mySprite = sprites.create(assets.image("""
    LINK
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
dr = sprites.create(assets.image("""
    myImage1
"""), SpriteKind.enemy)
info.set_life(3)
enemyspeed = 50
mySprite.ay = 1000
scene.camera_follow_sprite(mySprite)
dr.follow(mySprite, 50)
tiles.set_current_tilemap(tilemap("""
    level
"""))
scene.set_background_color(6)
tiles.place_on_random_tile(mySprite, sprites.swamp.swamp_tile0)
picture = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . f f . . . . . . . . 
            . . . . . f f f f . . . . . . . 
            . . . . . f f f f . . . . . . . 
            . . . . . . f f . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.projectile)
picture.follow(dr, 10)
mySprite2.follow(picture, 50)

def on_update_interval():
    global enemyspeed, d, mySprite2
    dr.set_velocity(enemyspeed, enemyspeed)
    enemyspeed += 1
    d = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 5 5 5 5 5 5 . . . . . . 
                    . . . 5 4 4 4 4 4 4 5 . . . . . 
                    . . . 5 4 5 5 5 5 4 5 . . . . . 
                    . . . 5 4 5 4 4 5 4 5 . . . . . 
                    . . . 5 4 5 5 5 5 4 5 . . . . . 
                    . . . 5 4 4 4 4 4 4 5 . . . . . 
                    . . . . 5 5 5 5 5 5 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    mySprite2 = sprites.create(img("""
            . . . . . 2 2 2 2 2 . . . . . . 
                    . . . . 2 2 2 2 2 2 2 . . . . . 
                    . . . . 2 2 2 9 9 9 9 9 . . . . 
                    . . 2 2 2 2 2 9 9 9 9 9 . . . . 
                    . . 2 2 2 2 2 9 9 9 9 9 . . . . 
                    . . 2 2 2 2 2 2 2 2 2 . . . . . 
                    . . 2 2 2 2 2 2 2 2 2 . . . . . 
                    . . 2 2 2 2 2 2 2 2 2 . . . . . 
                    . . . . 2 2 2 2 2 2 2 . . . . . 
                    . . . . 2 2 2 2 2 2 2 . . . . . 
                    . . . . 2 2 2 2 2 2 2 . . . . . 
                    . . . . 2 2 2 2 2 2 2 . . . . . 
                    . . . . . 2 2 . 2 2 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.MOGUS)
game.on_update_interval(5000, on_update_interval)

def on_forever():
    music.play_melody("E D G F B A C5 B ", 120)
    d.follow(dr, 50)
forever(on_forever)

def on_update_interval2():
    info.change_score_by(1)
game.on_update_interval(200, on_update_interval2)
