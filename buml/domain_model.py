####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Classes
Cliente = Class(name="Cliente")
Cuenta = Class(name="Cuenta")

# Cliente class attributes and methods
Cliente_id_de_cliente: Property = Property(name="id_de_cliente", type=IntegerType, visibility="private")
Cliente_nombre_cliente: Property = Property(name="nombre_cliente", type=StringType, visibility="private")
Cliente_numero_cuenta: Property = Property(name="numero_cuenta", type=StringType, visibility="private")
Cliente_m_insetar_tarjeta: Method = Method(name="insetar_tarjeta", parameters={Parameter(name='param', type=IntegerType)}, type=IntegerType, implementation_type=MethodImplementationType.NONE)
Cliente.attributes={Cliente_id_de_cliente, Cliente_nombre_cliente, Cliente_numero_cuenta}
Cliente.methods={Cliente_m_insetar_tarjeta}

# Cuenta class attributes and methods
Cuenta_numero_cuenta: Property = Property(name="numero_cuenta", type=StringType, visibility="private")
Cuenta_saldo: Property = Property(name="saldo", type=FloatType, visibility="private")
Cuenta_activa: Property = Property(name="activa", type=BooleanType, visibility="private")
Cuenta_m_method: Method = Method(name="method", parameters={}, implementation_type=MethodImplementationType.NONE)
Cuenta.attributes={Cuenta_activa, Cuenta_numero_cuenta, Cuenta_saldo}
Cuenta.methods={Cuenta_m_method}

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Cliente, Cuenta},
    associations={},
    generalizations={},
    metadata=None
)
