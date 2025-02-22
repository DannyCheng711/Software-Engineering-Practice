from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


# submit name and age
@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


def is_prime(n):
    """Returns True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def process_query(q):
    if q == "What is your name?":
        return "Computing genius"

    elif q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"

    elif "plus" in q:
        numbers = re.findall(r"\d+", q)
        if len(numbers) == 2:
            num1, num2 = int(numbers[0]), int(numbers[1])
            result = num1 + num2
            return f"{result}"

        if len(numbers) == 3:
            num1, num2, num3 = (
                int(numbers[0]),
                int(numbers[1]),
                int(numbers[2]),
            )
            result = num1 + num2 + num3
            return f"{result}"

    elif "largest" in q:

        numbers = re.findall(r"\d+(?:\.\d+)*", q)

        # 解析每个数字的最大子数
        if numbers:
            max_value = None
            for num in numbers:
                sub_values = [float(part) for part in num.split(".")]
                largest_sub_value = max(sub_values)

                if max_value is None or largest_sub_value > max_value:
                    max_value = largest_sub_value
            return (
                str(int(max_value))
                if max_value.is_integer()
                else str(max_value)
            )

    elif "multiplied" in q:
        numbers = re.findall(r"\d+", q)
        if len(numbers) == 2:
            num1, num2 = int(numbers[0]), int(numbers[1])
            result = num1 * num2
            return f"{result}"

    elif "both a square and a cube" in q:
        # 匹配并检查数字列表
        numbers = re.findall(r"\d+", q)

        valid_numbers = []
        for num_str in numbers:
            num = int(num_str)
            # 检查是否是完全六次方数
            root = round(num ** (1 / 6))
            if root**6 == num:
                valid_numbers.append(num_str)

        valid_numbers.sort()

        return (
            ", ".join(valid_numbers) if valid_numbers else "No numbers found"
        )

    elif "are primes" in q:
        numbers = re.findall(r"\d+", q)

        numbers = sorted(numbers)

        primes = [num for num in numbers if is_prime(int(num))]

        if primes:
            return f"{', '.join(map(str, primes))}"
        else:
            return "No prime numbers found."

    elif "minus" in q:
        numbers = re.findall(r"\d+", q)
        if len(numbers) >= 2:
            result = int(numbers[0]) - int(numbers[1])
            return str(result)

    elif "to the power of" in q:
        numbers = re.findall(r"\d+", q)
        if len(numbers) == 2:
            base, exponent = int(numbers[0]), int(numbers[1])
            result = base**exponent
        return str(result)

    else:
        return "Unknown"


# get the dinosaurs
@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    response = process_query(q)

    return response
