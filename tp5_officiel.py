"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random

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
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        #CRÉATION DU PYLONE
        arcade.draw.draw_lrbt_rectangle_filled(
            0,
            SCREEN_WIDTH,
            0,
            SCREEN_HEIGHT / 2.2,
            arcade.csscolor.DIM_GRAY)

        y = SCREEN_HEIGHT / 2 + 40
        arcade.draw.draw_triangle_filled(420, y + 260,
                                         370, y + 110,
                                         470, y + 110,
                                         arcade.color.SKY_BLUE)
        arcade.draw.draw_triangle_filled(420, y +0,
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

        arcade.draw_circle_filled( 420,y + 105, 10, arcade.color.BLUEBERRY )

        arcade.draw.draw_arc_filled(490, y + 110, 30, 120, arcade.csscolor.GOLD, 0, 90)
        arcade.draw.draw_arc_filled(490, y + 110, 30, 120, arcade.csscolor.GOLD, 270, 360)

        arcade.draw.draw_arc_filled(350, y + 110, 30, 120, arcade.csscolor.GOLD, 90, 180)
        arcade.draw.draw_arc_filled(350, y + 110, 30, 120, arcade.csscolor.GOLD, 180, 270)

        #création des canons

        r = arcade.rect.XYWH(180, y -62, 180, 25)
        arcade.draw.draw_rect_filled(r, arcade.csscolor.GOLD)
        arcade.draw.draw_arc_filled(180, y -70, 35, 105, arcade.csscolor.GOLD,0 ,180 )
        arcade.draw.draw_arc_filled(250, y -70, 35, 95, arcade.csscolor.GOLD,0 ,90 )
        arcade.draw.draw_arc_filled(110, y -70, 35, 95, arcade.csscolor.GOLD,90 ,180 )

        r = arcade.rect.XYWH(650, y -62, 180, 25)
        arcade.draw.draw_rect_filled(r, arcade.csscolor.GOLD)
        arcade.draw.draw_arc_filled(650, y -70, 35, 105, arcade.csscolor.GOLD,0 ,180 )
        arcade.draw.draw_arc_filled(720, y -70, 35, 95, arcade.csscolor.GOLD,0 ,90 )
        arcade.draw.draw_arc_filled(580, y -70, 35, 95, arcade.csscolor.GOLD,90 ,180 )

        arcade.draw_circle_filled(180, y + 45, 35, arcade.color.GOLD)
        arcade.draw_circle_filled(650, y + 45, 35, arcade.color.GOLD)

        arcade.draw.draw_line(150, y+65, 205, y+20, arcade.color.DARK_SLATE_GRAY, 2)
        arcade.draw.draw_line(155, y+20, 210, y+65, arcade.color.DARK_SLATE_GRAY, 2)
        arcade.draw.draw_line(620, y+65, 675, y+20, arcade.color.DARK_SLATE_GRAY, 2)
        arcade.draw.draw_line(625, y+20, 680, y+65, arcade.color.DARK_SLATE_GRAY, 2)
        arcade.draw_circle_filled(180, y + 40, 8, arcade.color.AQUA)
        arcade.draw_circle_filled(650, y + 40, 8, arcade.color.AQUA)




    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.clear()
    def on_key_press(self, key, key_modifiers):
        """-
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


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


if __name__ == "__main__":
    main()
