from pymongo import MongoClient
import time
from bson import ObjectId

mongo = MongoClient()


def timestamp():
    return time.time()


class Mongo(object):
    __fields__ = [
        ('type', str, ''),
        ('deleted', bool, False),
        ('message', str, ''),
        ('ct', str, ''),
        ('ut', str, ''),
    ]

    def get_id(self):
        return getattr(self, '_id', None)

    def get_type(self):
        return getattr(self, 'type', None)

    def if_deleted(self):
        return getattr(self, 'deleted', None)

    def get_message(self):
        return getattr(self, 'message', None)

    def get_ut(self):
        return getattr(self, 'ut', None)

    def get_ct(self):
        return getattr(self, 'ct', None)

    @classmethod
    def make_object(cls, query):
        m = cls()
        for key, value in query.items():
            setattr(m, key, value)
        return m

    @classmethod
    def _find(cls, **kwargs):
        # 类内部最基础的查找数据的方法
        name = cls.__name__
        flag_sort = '__sort'
        # 如果传入'__sort'参数可以实现不同形式的排序
        sort = kwargs.pop(flag_sort, None)
        ds = mongo.db[name].find(kwargs)
        if sort is not None:
            ds = ds.sort(sort)
        query_list = [cls.make_object(i) for i in ds]
        return query_list

    @classmethod
    def insert(cls, form=None, **kwargs):
        name = cls.__name__
        m = cls()
        fields = cls.__fields__.copy()
        if form is None:
            form = {}

        # 遍历表单, 如果表单里有model里要的值, 那么设置成表单里的,否则设置成默认值
        for f in fields:
            k, t, v = f
            if k in form and form[k]:
                setattr(m, k, t(form[k]))
            else:
                setattr(m, k, v)

        # 处理额外的参数, 如果模型里有, 则设置, 没有抛出错误
        for k, v in kwargs.items():
            if hasattr(m, k):
                setattr(m, k, v)

        # 设置默认时间, 类型
        m.ct = timestamp()
        m.type = name.lower()
        m.save()
        return m

    def save(self):
        # 用当前对象的成员变量保存为记录
        name = self.__class__.__name__
        setattr(self, 'ut', timestamp())
        mongo.db[name].save(self.__dict__)

    def update(self, form, hard=False):
        for k, v in form.items():
            if hard or hasattr(self, k):
                setattr(self, k, v)
        self.save()

    @classmethod
    def find_one(cls, **kwargs):
        a = cls._find(**kwargs)
        if a:
            return a[0]

    @classmethod
    def find_by(cls, **kwargs):
        # 通过_find找到所有符合要求的数据返回
        return cls._find(**kwargs)

    @classmethod
    def find_all(cls):
        return cls._find()

    @classmethod
    def find_by_id(cls, id):
        return cls.find_by(_id=ObjectId(id))[0]

    @classmethod
    def update_or_new(cls, form, **kwargs):
        # kwargs 为关键字, 找到则用form更新, 否则新建插入
        m = cls.find_one(**kwargs)
        if m:
            m.update(form, hard=True)
        else:
            m = cls.insert(form)
        return m

    @classmethod
    def aggregate(cls, func, key):
        res = {}
        query = cls.find_all()
        for item in query:
            if getattr(item, key, '') not in res:
                res[getattr(item, key, '')] = []
            res[getattr(item, key, '')].append(item)

        for key, value in res.items():
            res[key] = func(value)
        return res

    # @classmethod
    # def aggregate(cls, func1, func2):
    #     # @ param func1: group以后的操作
    #     # @ param func2: group依据, 接受一个model对象的list, 返回一个字典, key自订, value是根据key确定的models list
    #     temp = func2(cls.find_all())
    #     res = {}
    #     for k, v in temp.items():
    #         res[k] = func1(v)
    #     return res


    # @classmethod
    # def aggregate(cls, func, *keys):
    #     res = {}
    #     query = cls.find_all()
    #     for item in query:
    #         index = ""
    #         for key in keys:
    #             index += '+' + str(getattr(item, key, ''))
    #         if str not in res:
    #             res[index] = []
    #         res[index].append(item)
    #
    #     for key, value in res.items():
    #         res[key] = func(value)
    #     return res




