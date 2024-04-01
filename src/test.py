from main import Figure


def test():
    app_test_circle = Figure(r=3, figure_type='круг',)
    app_test_trangele = Figure(
        f_side=3,
        s_side=4,
        t_side=5,
        figure_type='треугольник')
    print(f'круг {app_test_circle.get_s_circle()} \n треугольник {app_test_trangele.get_s_triangle()} \n {app_test_trangele.check_tringle_right_or_not()}')


test()
