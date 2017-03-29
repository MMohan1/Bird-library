from birds import birds_api
from birds.router.resourcer import Birds

def get_resourcer(name, klass):
    dup_class = type(name+klass.__name__, klass.__bases__, dict(klass.__dict__))
    setattr(dup_class, 'ref_name', name)
    return dup_class


birds_api.add_resource(get_resourcer('birds', Birds), '/api/v1.0/birds','/api/v1.0/birds/<id>')
