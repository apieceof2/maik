from .mongo import Mongo


class Income(Mongo):
    __fields__ = Mongo.__fields__ + [
        # 仅仅包括基本信息, Payment字段通过mongo.update() 加入
        ('date', str, ''),
        ('car', str, ''),
        ('route', str, ''),
        ('revenue', float, 0),
        ('cashier', str, ''),
        ('remnant_num', int, 0),
        ('remnant_value', float, 0),
        ('fake_num', int, 0),
        ('fake_value', float, 0),
        ('people_num_by_cash', int, 0),
        ('people_num_by_cal', int, 0),
        ('people_num_by_car', int, 0),
    ]

    def income_sum(self):
        """
        return sum of the revenue and variety kind of payment income
        :return: float
        """
        return getattr(self, 'revenue', 0.0) + self.payment_sum()

    def payment_sum(self):
        """
        return sum of all kind of payment incom
        :return: float
        """
        # get the list of all kind of payment
        from models.payment import Payment
        payments = [getattr(p, 'name') for p in Payment.find_all()
                    if getattr(p, 'name') != getattr(p, 'payment_type') + '合计']

        # add all of the value of the payment fields
        sum = 0.0
        for payment in payments:
            value = getattr(self, payment, 0.0)[1]
            if not value:
                value = 0
            sum += value

        return sum

    def income_num_sum(self):
        """
        return the number of ] of all passager
        :return: int
        """
        return getattr(self, 'people_num_by_cash', 0) + self.payment_num_sum()

    def payment_num_sum(self):
        """
        return the number of the passager payed by other ways
        :return: int
        """
        # get the list of all kind of payment
        from models.payment import Payment
        payments = [getattr(p, 'name') for p in Payment.find_all()
                    if getattr(p, 'name') != getattr(p, 'payment_type')+'合计']

        # add all of the value of the payment fields
        sum = 0.0
        for payment in payments:
            value = getattr(self, payment, 0.0)[0]
            if not value:
                value = 0
            sum += value
        return sum






