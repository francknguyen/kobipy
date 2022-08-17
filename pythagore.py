from manim import *
import numpy as np


class Pythagore(Scene):
    def construct(self):
        self.camera.background_color = "#222222"

        #Titre + énoncé du théorème
        titre = Text(
            "Théorème de Pythagore",
            weight = BOLD
        ).scale(1.6)
        enonce = Text("Enoncé du théorème").scale(0.75).shift(3.5*UP + 3.5*LEFT)
        self.add(titre)
        self.wait(1)
        self.play(
            ReplacementTransform(titre, enonce),
            run_time=2
        )
        A, B, C = ORIGIN, RIGHT*4, UP*3
        cote1 = Line(A, B).set_color(RED).set_stroke(width = 2)
        cote2 = Line(A, C).set_color(BLUE).set_stroke(width = 2)
        hypotenuse = Line(B, C).set_color(GREEN).set_stroke(width = 2)
        angle_droit = RightAngle(cote1, cote2, stroke_width = 0.9).scale(0.9)
        group = VGroup(cote1, cote2, hypotenuse, angle_droit).move_to(2*LEFT + 0.25*DOWN).scale(0.5)
        
        self.play(
            GrowFromCenter(group), 
            run_time = 2
        )
        triangle_legende = MathTex("a", "b", "c").scale(1)
        triangle_legende[0].next_to(cote2, LEFT, buff=0.25).set_color(BLUE)
        triangle_legende[1].next_to(cote1, DOWN, buff=0.25).set_color(RED)
        triangle_legende[2].next_to(hypotenuse, RIGHT, buff=-0.6).set_color(GREEN).shift(0.2*UP)

        self.play(Write(triangle_legende), run_time=1.5)
        self.wait()

        objectif = MathTex("c^2", "=", "a^2", "+", "b^2").move_to(2*RIGHT)
        objectif[0].set_color(GREEN)
        objectif[2].set_color(BLUE)
        objectif[4].set_color(RED)
        # texte = Text("Objectif : ").scale(0.5).next_to(objectif, UP, buff=0.5)
        # self.play(FadeIn(texte))
        self.play(
            ReplacementTransform(VGroup(hypotenuse.copy(), triangle_legende[2].copy()), objectif[0]),
            ReplacementTransform(VGroup(cote2.copy(), triangle_legende[0].copy()), objectif[2]),
            ReplacementTransform(VGroup(cote1.copy(), triangle_legende[1].copy()), objectif[4]), 
            Create(VGroup(objectif[1], objectif[3])),
            run_time=1
        )
        self.wait(2)
        self.play(FadeOut(objectif, enonce, triangle_legende, group))

        demonstration = Text("Démonstration").scale(0.75).shift(3.5*UP + 4*LEFT)
        self.play(Create(demonstration))
        self.wait(1)

        A, B, C = ORIGIN, RIGHT*4, UP*3
        triangle = Polygon(*[A, B, C], color=BLUE, fill_color=BLUE, fill_opacity=0.2, stroke_width=2).scale(0.5)
        triangle.move_to(ORIGIN, aligned_edge=ORIGIN)
        triangle_copie1 = triangle.copy().move_to(UL*2)
        triangle_copie2 = triangle.copy().move_to(UR*2)
        triangle_copie3 = triangle.copy().move_to(DL*2)
        triangle_copie4 = triangle.copy().move_to(DR*2)
        all_copies = [triangle_copie1, triangle_copie2, triangle_copie3, triangle_copie4]

        triangle_legende = MathTex("a", "b", "c").scale(0.75)
        #triangle_legende.set_color_by_tex_to_color_map({"a":RED, "b":GOLD, "c":PINK})
        triangle_legende[0].next_to(triangle.get_left(), LEFT, buff=0.25)
        triangle_legende[1].next_to(triangle.get_bottom(), DOWN, buff=0.25)
        triangle_legende[2].next_to(triangle.get_top(), UP, buff=-0.5)

        self.play(Create(triangle),run_time=1)
        self.play(Write(triangle_legende), run_time=1)
        self.wait(2)
        self.play(FadeOut(triangle_legende))

        self.wait()
        self.play(
            ReplacementTransform(triangle, VGroup(*all_copies)), 
            run_time=3
        )

        self.play(
            Rotating(triangle_copie1, radians=+PI/2 , about_point=triangle_copie1.get_center_of_mass(), run_time=0.5),
            Rotating(triangle_copie2, radians=2*PI, about_point=triangle_copie2.get_center_of_mass(), run_time=0.5),
            Rotating(triangle_copie3, radians=-PI, about_point=triangle_copie3.get_center_of_mass(), run_time=0.5),
            Rotating(triangle_copie4, radians=-PI/2, about_point=triangle_copie4.get_center_of_mass(), run_time=0.5)
        )
        self.play(triangle_copie1.animate.move_to(ORIGIN, aligned_edge=DR))
        self.play(triangle_copie2.animate.move_to(ORIGIN + UP*0.5, aligned_edge=DL))
        self.play(triangle_copie3.animate.move_to(ORIGIN + RIGHT*0.5, aligned_edge=UR))
        self.play(triangle_copie4.animate.move_to(ORIGIN + RIGHT*0.5 + UP*0.5, aligned_edge=UL))
        self.wait()

        carre = Square(side_length=0.5, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5, stroke_width=1)
        carre.move_to(ORIGIN, aligned_edge=DL)
        self.play(Create(carre))
        #self.play(GrowFromCenter(carre), run_time=2)
        all_figure = VGroup(*all_copies, carre)
        sommets_exterieur = [
            triangle_copie1.get_vertices()[1], 
            triangle_copie1.get_vertices()[2], 
            triangle_copie4.get_vertices()[1],
            triangle_copie4.get_vertices()[2]
        ]
        carre_exterieur = Polygon(*sommets_exterieur, color=RED, fill_color=RED, fill_opacity=0)
        #self.play(Rotating(all_figure, radians=0.64, about_point=carre_exterieur.get_center(), run_time=0.5))

        
        """ for sommet, couleur in zip(sommets_exterieur, [BLUE, RED, PINK, PINK]):
            #self.add(Dot(sommet, couleur))
            self.add(Dot(point=sommet, color=couleur)) """

        self.add(carre_exterieur)
        self.play(
            carre_exterieur.animate.shift(LEFT*3).set_opacity(0.3),
            all_figure.animate.shift(RIGHT*3),
        )
        self.play(
            carre_exterieur.animate.shift(UP).set_opacity(0.3),
            all_figure.animate.shift(UP),
        )
        
        self.wait()

        self.play(Indicate(carre_exterieur, color=PINK, run_time=2))

        legende = Tex(
            "Aire(", 
            ")", 
            "=", 
            "4\,",
            "Aire(",
            ")",
            "+", 
            "Aire(",
            ")")
        legende.scale(0.75)

        legende[0].next_to(carre_exterieur, DOWN*3, aligned_edge=LEFT)
        petit_carre_exterieur = carre_exterieur.copy().scale(0.2).next_to(legende[0], RIGHT)
        legende[1].next_to(petit_carre_exterieur, RIGHT)
        self.play(
            FadeIn(legende[0], shift=LEFT),
            ReplacementTransform(carre_exterieur.copy(), petit_carre_exterieur),
            FadeIn(legende[1], shift=RIGHT)
        )

        legende[2].next_to(legende[1], buff=2)
        self.play(Write(legende[2]))

        legende[3:5].next_to(legende[2], buff=2)
        petit_triangle = triangle_copie1.copy().scale(0.2).next_to(legende[4], RIGHT)
        legende[5].next_to(petit_triangle, RIGHT)
        self.play(Indicate(VGroup(*all_copies), color=PINK, run_time=2))
        self.play(
            FadeIn(legende[3:5], shift=LEFT),
            ReplacementTransform(VGroup(triangle_copie1.copy(), triangle_copie2.copy(), triangle_copie3.copy(), triangle_copie4.copy()), petit_triangle),
            FadeIn(legende[5], shift=RIGHT)
        )

        legende[6].next_to(legende[5], RIGHT)
        self.play(FadeIn(legende[6], shift=LEFT))

        legende[7].next_to(legende[6], RIGHT)
        petit_carre = carre.copy().scale(0.2).next_to(legende[7], RIGHT)
        legende[8].next_to(petit_carre, RIGHT)
        self.play(Indicate(carre), color=PINK, run_time=2)
        self.play(
            FadeIn(legende[7], shift=LEFT),
            ReplacementTransform(carre.copy(), petit_carre),
            FadeIn(legende[8], shift=LEFT)
        )
        self.wait()

        #affichage de c et c^2
        brace_c1 = Brace(Line(triangle_copie1.get_vertices()[1], triangle_copie2.get_vertices()[1]), direction=[0.75, 1, 0], sharpness=1)
        c1_legend = brace_c1.get_tex("c").scale(0.75) 
        brace_c = Brace(Line(carre_exterieur.get_vertices()[0], carre_exterieur.get_vertices()[-1]), direction=[0.75, 1, 0], sharpness=1)
        c_legend = brace_c.get_tex("c").scale(0.75)
        self.play(Circumscribe(VGroup(legende[0:2], petit_carre_exterieur), fade_out=True), run_time=1)
        self.play(
            FadeIn(VGroup(brace_c, c_legend, brace_c1, c1_legend), shift=DOWN)
        )
        self.wait(1)
        aire_carre = MathTex("c^2").scale(0.75).next_to(carre_exterieur, DOWN*3)
        self.play(
            ReplacementTransform(VGroup(legende[0:2], petit_carre_exterieur, c_legend, brace_c, c1_legend, brace_c1), aire_carre), run_time=2
        )

        self.wait()

        #affichage de a, b et aire(triangle)
        brace_a = Brace(Line(triangle_copie1.get_vertices()[2], triangle_copie1.get_vertices()[1]), direction=[0, -1, 0], sharpness=1)
        brace_b = Brace(Line(triangle_copie1.get_vertices()[0], triangle_copie1.get_vertices()[1]), direction=[1, 0, 0], sharpness=1)
        a_legend = brace_a.get_tex("a").scale(0.75)
        b_legend = brace_b.get_tex("b").scale(0.75)
        self.play(Circumscribe(VGroup(legende[3:6], petit_triangle), fade_out=True), run_time=1)
        self.play(
            FadeIn(VGroup(brace_a, a_legend), shift=UP),
            FadeIn(VGroup(brace_b, b_legend), shift=LEFT)
        )
        self.wait(0.5)
        aire_triangle = MathTex("4\\times\dfrac{ab}{2}\quad").scale(0.75).next_to(legende[6], LEFT)
        simplification = MathTex("2ab").scale(0.75).next_to(legende[6], LEFT)
        self.play(
            ReplacementTransform(VGroup(legende[3:6], petit_triangle, a_legend, b_legend, brace_a, brace_b), aire_triangle), run_time=2
        )

        self.wait(1)

        self.play(
            ReplacementTransform(aire_triangle, simplification), run_time=2
        )

        self.wait(1)

        #affichage de c et c^2
        brace_a1 = Brace(Line(triangle_copie4.get_vertices()[1] + 2*UP, triangle_copie4.get_vertices()[2] + 2*UP), direction=[0, -1, 0], sharpness=1)
        brace_b1 = Brace(Line(triangle_copie2.get_vertices()[1], triangle_copie2.get_vertices()[0]), direction=[0, 1, 0], sharpness=1)
        a1_legend = brace_a1.get_tex("a").scale(0.75)
        b1_legend = brace_b1.get_tex("b").scale(0.75)
        self.play(Circumscribe(VGroup(legende[7:9], petit_carre), fade_out=True), run_time=1)
        self.play(
            FadeIn(VGroup(brace_a1, a1_legend), shift=DOWN),
            FadeIn(VGroup(brace_b1, b1_legend), shift=UP)
        )
        self.wait(0.5)
        brace_ab = Brace(Line(carre.get_vertices()[0], carre.get_vertices()[1]), direction=[0, 1, 0], sharpness=4)
        ab_legend = brace_ab.get_tex("b-a").scale(0.75)
        self.play(
            ReplacementTransform(VGroup(brace_a1, a1_legend, brace_b1, b1_legend), VGroup(brace_ab, ab_legend)), run_time=2
        )
        self.wait(1)
        aire_petit_carre = MathTex("(b-a)^2").scale(0.75).next_to(legende[6], RIGHT)
        simplification1 = MathTex("b^2-2ab+a^2").scale(0.75).next_to(legende[6], RIGHT)
        self.play(
            ReplacementTransform(VGroup(legende[7:9], petit_carre, ab_legend, brace_ab), aire_petit_carre), run_time=2
        )
        self.wait(1)
        self.play(
            ReplacementTransform(aire_petit_carre, simplification1), run_time=2
        )

        self.wait(2)

        simplification_finale = MathTex("a^2+b^2").scale(0.75).next_to(legende[2], RIGHT, buff=2)
        self.play(ReplacementTransform(VGroup(legende[6], simplification, simplification1), simplification_finale), run_time=2)
        self.wait()

        formule = MathTex("c^2=a^2+b^2").next_to(legende[2])
        self.play(
            ReplacementTransform(VGroup(simplification_finale, legende[2], aire_carre), formule, run_time=2)
        )
        self.play(Circumscribe(formule, time_width=3, FadeOut=False))

        self.wait()
