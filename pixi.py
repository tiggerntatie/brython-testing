from javascript import JSObject, JSConstructor
from browser import document, alert, window

PIXI = JSObject(window.PIXI)
Stage = JSConstructor(window.PIXI.Stage)
Sprite = JSConstructor(window.PIXI.Sprite)
GRAPHICS = JSConstructor(window.PIXI.Graphics)


