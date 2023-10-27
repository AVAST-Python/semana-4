# Ajusta esto para que la ventana aparezca en el monitor y en la posición que quieras
POSITION = dict(
    POSICION_DESDE_LA_IZQUIERDA = 500,
    POSICION_DESDE_ARRIBA = 0,
    ANCHO_VENTANA = 1024,
    ALTO_VENTANA = 900
    )

def position_screen(t):
    t.screen.setup(
        width=POSITION['ANCHO_VENTANA'],
        height=POSITION['ALTO_VENTANA'],
        startx=POSITION['POSICION_DESDE_LA_IZQUIERDA'],
        starty=POSITION['POSICION_DESDE_ARRIBA']
        )
