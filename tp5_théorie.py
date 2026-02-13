import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WINDOW_TITLE = "Tutoriel Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
arcade.draw.draw_lrbt_rectangle_filled(
    0,
    SCREEN_WIDTH,
    0,
    SCREEN_HEIGHT / 2,
    arcade.csscolor.DARK_GREEN)

r = arcade.rect.XYWH(200, SCREEN_HEIGHT / 2, 30, 60)
arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)

arcade.draw.draw_circle_outline(200, 200, 60, arcade.color.BUBBLE_GUM, num_segments=8, tilt_angle=35)
arcade.draw.draw_circle_outline(400, 200, 60, arcade.color.BUBBLE_GUM, num_segments=8)

arcade.draw.draw_arc_filled(400, SCREEN_HEIGHT / 2 + 20, 60, 100, arcade.csscolor.FOREST_GREEN, 0, 180)

y = SCREEN_HEIGHT / 2 + 40
arcade.draw.draw_triangle_filled(500, y + 40,
                           470, y - 20,
                           530, y - 20,
                           arcade.color.FOREST_GREEN)

arcade.draw.draw_line(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 110, SCREEN_WIDTH, SCREEN_HEIGHT - 110, arcade.color.BANANA_YELLOW, 10)

points = [(700, 300), (750, 600), (345, 675)]
arcade.draw.draw_line_strip(points, arcade.color.BUFF)

# Voici un tuple avec trois valeurs: un chiffre entier, une booléenne #
# ainsi qu'une liste qui contient deux string.
un_tuple = (23, True, ["a", "b"])
    
# Dans l'exemple ci-dessous, il y a une liste de coordonnées. Chaque tuple représente
# une valeur pour le X ainsi qu'une pour le Y
points = [(700, 300), (750, 600), (345, 675)]

# Dans la liste ci-dessous, chaque paire de tuple représente le point de départ
# d'une ligne ainsi que le point d'arrivée. Ainsi, la première ligne commence
# à 139,556 et se termine à 720, 512.
line_list = [(139, 556), (720, 512), (773, 704), (710, 596)]
arcade.draw.draw_lines(line_list, arcade.color.FOREST_GREEN)

points = [(700, 300), (750, 600), (345, 675)]
arcade.draw.draw_polygon_filled(points, arcade.color.AERO_BLUE)

points = [(200, 200), (350, 200), (345, 375), (23, 224), (222, 222)]
arcade.draw.draw_polygon_outline(points, arcade.color.ALIZARIN_CRIMSON, 10)

affichage = arcade.Text("Ceci est une chaîne de caractère!", 20, SCREEN_HEIGHT - 40, arcade.color.BARBIE_PINK)
affichage.draw()


arcade.finish_render()

arcade.run()
def main():

   arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")


main()