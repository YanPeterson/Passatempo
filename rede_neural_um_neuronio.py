import math

input = -1

output_desire = 2

input_weight = 0.5

leanirg_rate = 0.1
def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada", input, "desejado", output_desire)

error = math.inf
iteration = 0

bias = 1
bias_weigth = 0.5

while not error == 0:
    print('peso', input_weight)
    iteration += 1
    sum = (input * input_weight) + (bias * bias_weigth)
    output = activation(sum)
    print('saida', output)
    error = output_desire - output
    print('error', error)

    if not error == 0:
        input_weight = input_weight + leanirg_rate * input * error
        bias_weigth = bias_weigth + (leanirg_rate * bias + error)
print("Sabe muito rede neural")
print(iteration)