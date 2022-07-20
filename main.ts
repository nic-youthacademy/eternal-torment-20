namespace SpriteKind {
    export const portal = SpriteKind.create()
    export const portal2 = SpriteKind.create()
    export const heart = SpriteKind.create()
    export const MOGUS = SpriteKind.create()
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`myImage3`)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    mySprite.setImage(assets.image`LINK`)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite3, otherSprite3) {
    pause(1000)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.MOGUS, function (sprite, otherSprite) {
    info.changeScoreBy(150)
    sprites.destroyAllSpritesOfKind(SpriteKind.MOGUS, effects.spray, 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite2, otherSprite2) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Food, effects.spray, 500)
    info.changeScoreBy(5)
})
let picture: Sprite = null
let mySprite2: Sprite = null
let d: Sprite = null
let mySprite: Sprite = null
Render.toggleViewMode()
mySprite = sprites.create(assets.image`LINK`, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
let dr = sprites.create(assets.image`myImage1`, SpriteKind.Enemy)
info.setLife(3)
let enemyspeed = 50
mySprite.ay = 1000
scene.cameraFollowSprite(mySprite)
dr.follow(mySprite, 50)
scene.setBackgroundImage(assets.image`myImage4`)
tiles.setCurrentTilemap(tilemap`level`)
scene.setBackgroundColor(10)
tiles.placeOnRandomTile(mySprite, sprites.swamp.swampTile0)
game.onUpdateInterval(5000, function () {
    dr.setVelocity(enemyspeed, enemyspeed)
    enemyspeed += 1
    d = sprites.create(img`
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
        `, SpriteKind.Food)
})
forever(function () {
    music.playMelody("E D G F B A C5 B ", 120)
    d.follow(dr, 50)
    mySprite2 = sprites.create(img`
        . . b b b b . . 
        . b 5 5 5 5 b . 
        b 5 d 3 3 d 5 b 
        b 5 3 5 5 1 5 b 
        c 5 3 5 5 1 d c 
        c d d 1 1 d d c 
        . f d d d d f . 
        . . f f f f . . 
        `, SpriteKind.MOGUS)
    picture = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . 2 . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Projectile)
    pause(5000)
    picture.follow(dr, 35)
    mySprite2.follow(picture, 30)
})
game.onUpdateInterval(200, function () {
    info.changeScoreBy(1)
})
