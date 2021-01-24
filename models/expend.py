from .mongo import Mongo


class Expend(Mongo):
    __fields__ = Mongo.__fields__ + [
        # 仅仅包括基本信息, Payment字段通过mongo.update() 加入
        ('date', str, ''),
        ('car', str, ''),
        ('route', str, ''),
    ]

    def get_by_key(self, key):
        t = getattr(self, key)
        if not t:
            return ''
        return t

    def get_resource(self, resource_name, index):
        """
        获得某一个reousrce下的第index个键值
        :param resource_name:
        :param key:
        :return:
        """
        resource = getattr(self, resource_name)
        if len(resource) < index + 1:
            if (resource_name == '亿通（加油站）2' or resource_name == '亿通（加油站）1') and index == 0:
                return ''
            else:
                return 0
        else:
            return resource[index]

    def get_resource_amount_sum(self, resource_type_name):
        """
        获得name 为 resource_type_name 的 资源的和
        :param resource_type_name:
        :return:
        """
        # 找到所有好友类型为resource_type_name的resource
        from models.resource import Resource
        resources = Resource.find_by(resource_type=resource_type_name)
        if resource_type_name == '充电站':
            a = 1
        if resource_type_name == '加气站':
            a = 1
        else:
            a = 2
        # 遍历, 把所有resources中有的字段中的数量加起来
        sum = 0
        for r in resources:

            sum += self.get_resource(getattr(r, 'name'), a)
        return sum

    def get_resource_price_sum(self, resource_type_name):
        """
        获得name 为 resource_type_name 的 资源的金额
        :param resource__type_name:
        :return:
        """
        # 找到所有好友类型为resource_type_name的resource
        from models.resource import Resource
        resources = Resource.find_by(resource_type=resource_type_name)
        if resource_type_name == '充电站':
            a = 2
        if resource_type_name == '加气站':
            a = 3
        else:
            a = 3

        # 遍历, 把所有resources中有的字段中的数量加起来
        sum = 0
        for r in resources:

            sum += self.get_resource(getattr(r, 'name'), a)
        return sum






