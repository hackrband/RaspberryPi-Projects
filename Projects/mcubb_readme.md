On the project **making_circuit_using_the_bread_board.py**,
if you are not satisfied with the buzzer noise, you can stop it by removing "18" from pin_a and pin_b:

python
```python
pin_a = [18, 23, 24, 25, 26] --> pin_a = [23, 24, 25, 26]
pin_b = [26, 25, 24, 23, 18] --> pin_b = [26, 25, 24, 23]
```

Cons:
First output on the array will become functionless.
