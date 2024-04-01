

class Figure:

    def __init__(self, r=None,
                 figure_type=None,
                 f_side=None,
                 s_side=None,
                 t_side=None) -> None:
        self.figure_type = figure_type
        self.pi = 3.14
        self.r = r
        self.f_side = f_side
        self.s_side = s_side
        self.t_side = t_side

    def get_s_circle(self) -> int:
        """Return cirlce area"""
        return self.pi * self.r ** 2

    def get_s_triangle(self) -> int:
        """Return triangle area"""
        p = (self.f_side + self.s_side + self.t_side) / 2
        return (p * (p - self.f_side) * (p - self.s_side) * (p - self.t_side)) ** 0.5

    def check_tringle_right_or_not(self) -> str:
        """Return print , trangle is right or not"""
        if (self.f_side*self.f_side + self.s_side*self.s_side == self.t_side*self.t_side) or (self.f_side*self.f_side + self.t_side*self.t_side == self.s_side*self.s_side) or (self.t_side*self.t_side + self.s_side*self.s_side == self.f_side*self.f_side):
            return ("треугольник прямоугольный")
        else:
            return ("треугольник не прямоугольный")


class Program:
    def __init__(self) -> None:
        self.figure_type = self._ask_figure_type()
        self.figure = Figure(figure_type=self.figure_type,
                             r=None, f_side=None, s_side=None, t_side=None)

    def run(self) -> None:
        """Run program"""
        if self.figure.figure_type == "круг":
            self.figure.r = int(input("Введите радиус: "))
            print(f"Площадь круга: {self.figure.get_s_circle()}")
        elif self.figure.figure_type == "треугольник":
            self.figure.f_side = int(input("Введите первую сторону: "))
            self.figure.s_side = int(input("Введите вторую сторону: "))
            self.figure.t_side = int(input("Введите третью сторону: "))

            print(
                f"Площадь треугольника: {self.figure.get_s_triangle()}\n {self.figure.check_tringle_right_or_not()}")

    def _ask_figure_type(self) -> str:
        """Ask client what type of figure"""
        figure_type = input("Введите тип фигуры: ")
        if figure_type not in ["круг", "треугольник"]:
            raise ValueError("Неверный тип фигуры")
        return figure_type


if __name__ == "__main__":
    app = Program()
    app.run()
