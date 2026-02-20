"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade

# création de la fenetrre de la page
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WINDOW_TITLE = "Aiur"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """
    def __init__(self):
        super().__init__()

        # If you have sprite lists, you should create them here,
        # and set them to None

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        # faire la couleur de fon
        arcade.set_background_color(arcade.color.BROWN)

        # CRÉATION DU PYLONE

        arcade.draw.draw_lrbt_rectangle_filled(
            0,
            SCREEN_WIDTH,
            0,
            SCREEN_HEIGHT / 2.2,
            arcade.csscolor.DARK_GREEN)

        y = SCREEN_HEIGHT / 2 + 40
        arcade.draw.draw_triangle_filled(420, y + 260,
                                         370, y + 110,
                                         470, y + 110,
                                         arcade.color.SKY_BLUE)
        arcade.draw.draw_triangle_filled(420, y + 0,
                                         370, y + 90,
                                         470, y + 90,
                                         arcade.color.SKY_BLUE)
        r = arcade.rect.XYWH(420, y + 105, 130, 25)
        arcade.draw.draw_rect_filled(r, arcade.csscolor.GOLD)

        arcade.draw.draw_triangle_filled(420, y + 135,
                                         410, y + 115,
                                         430, y + 115,
                                         arcade.color.GOLD)

        arcade.draw.draw_triangle_filled(420, y + 70,
                                         410, y + 90,
                                         430, y + 90,
                                         arcade.color.GOLD)

        arcade.draw_point(405, y + 105, arcade.color.DARK_BLUE, 5)
        arcade.draw_point(435, y + 105, arcade.color.DARK_BLUE, 5)

        arcade.draw_circle_filled(420, y + 105, 10, arcade.color.BLUEBERRY)

        arcade.draw.draw_arc_filled(490, y + 110, 30, 120, arcade.csscolor.GOLD, 0, 90)
        arcade.draw.draw_arc_filled(490, y + 110, 30, 120, arcade.csscolor.GOLD, 270, 360)

        arcade.draw.draw_arc_filled(350, y + 110, 30, 120, arcade.csscolor.GOLD, 90, 180)
        arcade.draw.draw_arc_filled(350, y + 110, 30, 120, arcade.csscolor.GOLD, 180, 270)

        points = [(370, y+118), (420, y+265), (470, y+118)]
        arcade.draw.draw_line_strip(points, arcade.color.DARK_BLUE)

        # faire le texte en haut de l'écran
        affichage = arcade.Text("Pylone et deux canon a photon!", 20, SCREEN_HEIGHT - 40, arcade.color.BARBIE_PINK)
        affichage.draw()
        # faire l'énergie s'émanent du pylone
        points = [(435, y+247), (437, y+245), (429, y+241), (441, y+239)]
        arcade.draw.draw_polygon_filled(points, arcade.color.DARK_BLUE)
        points = [(435, y+238), (437, y+238), (439, y+236), (441, y+234)]
        arcade.draw.draw_polygon_filled(points, arcade.color.DARK_BLUE)
        points = [(405, y+247), (407, y+243), (409, y+241), (411, y+239)]
        arcade.draw.draw_polygon_filled(points, arcade.color.DARK_BLUE)
        points = [(405, y+238), (407, y+238), (409, y+236), (411, y+234)]
        arcade.draw.draw_polygon_filled(points, arcade.color.DARK_BLUE)

        # création des canons

        arcade.draw.draw_ellipse_filled(180, y - 47, 175, 12, arcade.color.BRONZE, 0)
        arcade.draw.draw_ellipse_filled(650, y - 47, 175, 12, arcade.color.BRONZE, 0)

        r = arcade.rect.XYWH(180, y - 62, 180, 25)
        arcade.draw.draw_rect_filled(r, arcade.csscolor.GOLD)
        arcade.draw.draw_arc_filled(180, y - 70, 35, 105, arcade.csscolor.GOLD, 0, 180)
        arcade.draw.draw_arc_filled(250, y - 70, 35, 95, arcade.csscolor.GOLD, 0,  90)
        arcade.draw.draw_arc_filled(110, y - 70, 35, 95, arcade.csscolor.GOLD, 90, 180)

        r = arcade.rect.XYWH(650, y - 62, 180, 25)
        arcade.draw.draw_rect_filled(r, arcade.csscolor.GOLD)
        arcade.draw.draw_arc_filled(650, y - 70, 35, 105, arcade.csscolor.GOLD, 0, 180)
        arcade.draw.draw_arc_filled(720, y - 70, 35, 95, arcade.csscolor.GOLD, 0, 90)
        arcade.draw.draw_arc_filled(580, y - 70, 35, 95, arcade.csscolor.GOLD, 90, 180)

        arcade.draw_circle_filled(180, y + 45, 35, arcade.color.GOLD)
        arcade.draw_circle_filled(650, y + 45, 35, arcade.color.GOLD)

        arcade.draw.draw_line(150, y+65, 205, y+20, arcade.color.BLACK, 4)
        arcade.draw.draw_line(155, y+20, 210, y+65, arcade.color.BLACK, 4)
        arcade.draw.draw_line(620, y+65, 675, y+20, arcade.color.BLACK, 4)
        arcade.draw.draw_line(625, y+20, 680, y+65, arcade.color.BLACK, 4)
        arcade.draw_circle_filled(180, y + 40, 8, arcade.color.AQUA)
        arcade.draw_circle_filled(650, y + 40, 8, arcade.color.AQUA)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.clear()


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


# éxécute tout le texte
if __name__ == "__main__":
    main()
