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





