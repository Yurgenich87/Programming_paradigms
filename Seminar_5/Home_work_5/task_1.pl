% Правило для вычисления суммы элементов списка
sum_list([], 0). % Базовый случай: сумма пустого списка равна 0
sum_list([Head|Tail], Sum) :- % Рекурсивное правило
    sum_list(Tail, Rest), % Рекурсивно вычисляем сумму хвоста списка
    Sum is Head + Rest. % Сумма списка равна первому элементу плюс сумма остальных элементов


?- sum_list([1,2,3,4,5,6,7,8,9,10], Sum).
