from math import floor

EPS = 1e-9


class DD1K:

    def __init__(self, _lambda, mu, k, initial_customers=0):
        self.__lambda = eval(_lambda)
        self.__mu = eval(mu)
        self.__k = int(k)
        self.__initial_customers = int(initial_customers)

        self.customer_limit = 100
        self.time_limit = 100

        self.customer_arrival_time = []  # DONE
        self.system_size_per_time = []  # DONE
        self.balking_list = {}  # DONE
        self.balking_customers = []  # DONE
        self.queue_time = []  # DONE
        self.total_time = []  # DONE
        self.departures = []  # DONE

        # calculating ti
        if self.__lambda > self.__mu:
            self.__ti = self.ti_case_1()
        elif self.__lambda == self.__mu:
            self.__ti = 0
        else:
            self.__ti = self.ti_case_2()

        # queue waiting time for each customer
        self.queue_time = [0] * self.customer_limit
        for i in range(self.customer_limit):
            self.queue_time[i] = self.wq(i)

        # calculate customer arrival time up to customers limit
        self.customer_arrival_time = [0] * self.customer_limit
        for i in range(1, self.customer_limit):
            self.customer_arrival_time[i] = self.customer_arrival_time[i - 1] + 1 / self.__lambda

        for i in range(self.customer_limit):
            self.total_time[i] = 1 / self.__mu + self.queue_time[i]
            self.departures[i] = self.total_time[i] + self.customer_arrival_time[i]

    @staticmethod
    def unstable_system():
        print("The queues will tend to infinity as Lambda is greater than 1 times Mu")

    # m here stands for initial customers number
    def f_without_m(self, t):
        return int(int(t * self.__lambda) - int((t * self.__mu) - (self.__mu / self.__lambda) + EPS))

    def f_with_m(self, t):
        return int(self.__initial_customers + floor(self.__lambda * t) - floor(self.__mu * t))

    def waiting_time_1(self, n):
        return int(1 / self.__mu - 1 / self.__lambda + EPS) * (n - 1)

    # {time when the service starts for customer n} – {time when the customer n arrives}
    def waiting_time_2(self, n):
        return (self.__initial_customers + n - 1) * (1 / self.__mu) - self.time_corresponding_to_customer(n)

    @property
    def first_balked_customer(self):
        return floor(self.customer_corresponding_to_time(self.get_ti()))

    def customer_corresponding_to_time(self, t):
        t = float(t)
        return int(self.__lambda * t)

    def time_corresponding_to_customer(self, customer):
        return floor(int(customer) / self.__lambda)

    # -- ti represents the time of occurrence of the first balk -- #
    def ti_case_1(self):
        # Find the integer value of ti using bi-section method
        _l, _r, _mid = 0, 1e10, 0
        while _l < _r:
            _mid = (_l + _r) // 2

            if self.__initial_customers == 0:
                small_k = self.f_without_m(_mid)
            else:
                small_k = self.f_with_m(_mid)

            if small_k == self.__k:
                _r = _mid
            elif small_k < self.__k:
                _l = _mid + 1
            else:
                _r = _mid - 1

        return int(_l)

    def ti_case_2(self):
        _l, _r, _mid = 0, 1e10, 0
        while _l < _r:
            _mid = (_l + _r) // 2
            small_k = floor(self.__mu * _mid) - floor(self.__lambda * _mid)
            if small_k == self.__initial_customers:
                _r = _mid
            elif small_k < self.__initial_customers:
                _l = _mid + 1
            else:
                _r = _mid - 1

        return int(_l)

    def is_lambda_mul_of_mu(self):
        temp = self.__lambda / self.__mu
        return temp - int(temp) < EPS

    # n(t)
    def nt(self, t):
        t = int(t)

    def average_waiting(self):
        return (self.__initial_customers - 1) / (2 * self.__mu)

    # Wq(n)
    def wq(self, n):
        if self.__lambda > self.__mu:
            if n == 0 and self.__initial_customers == 0:
                return 0
            elif n == 0 and self.__initial_customers != 0:
                return self.average_waiting()

    def set_lambda(self, _lambda):
        self.__lambda = eval(_lambda)

    def set_mu(self, mu):
        self.__mu = eval(mu)

    def set_k(self, k):
        self.__k = int(k)

    def set_initial_customers(self, initial_customers):
        self.__initial_customers = int(initial_customers)

    def set_customer_limit(self, cl):
        self.customer_limit = int(cl)

    def set_time_limit(self, t):
        self.time_limit = int(t)

    def get_lambda(self):
        return self.__lambda

    def get_mu(self):
        return self.__mu

    def get_k(self):
        return self.__k

    def get_initial_customers(self):
        return self.__initial_customers

    def get_ti(self):
        return self.__ti
