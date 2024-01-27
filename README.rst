=================================
Automation Mojo Extension Package
=================================

This is a python package that provides a mechanism for extending other python packages.  This
package is different from other python extension packages in that it uses the python Protocol
typing in order to query module hierarchies for extensions.


===============================
Declaring an Extension Protocol
===============================

For example, if we want to be able to create instance of object like these from a factory.

.. code:: python

    class Hey:
        def __str__(self):
            return "Hey"

    class Ho:
        def __str__(self):
            return "Ho"

    
    # The following class defines a protocol that defines an extenstion type.
    # Extensions 

    class MyExtTypeProtocol(ExtProtocol):

        ext_protocol_name = "mojo-myextypeprotocol"

        @classmethod
        def give_me_a_hey(cls):
            ...

        @classmethod
        def give_me_a_ho(cls):
            ...

==================================
Implementing an Extension Protocol
==================================

The code below is implementing the extension protocol defined above.  When a class
implements an extension protocol, it will inherit from the protocol it is implementing.
By inheriting from the protocol, it pulls in the `ext_protocol_name` variable which
ensures that the derived type is declared to implement a given protocol.

Another important thing to look at in the code below is the class variable `PRECEDENCE`.
The `PRECEDENCE` number indicates to the SuperFactory which extensions to return when
an extension is queried based on precedence of overload and relevance.  The higher number
precedence is considered by the SuperFactory to have the most relevance.

.. code:: python

    class MyExtTypeFactory(ExtFactory, MyExtTypeProtocol):

        PRECEDENCE = 10

        @classmethod
        def give_me_a_hey(cls):
            return Hey
        
        @classmethod
        def give_me_a_ho(cls):
            return Ho


===================================
Configuration for Custom Extensions
===================================

In order to be able to extend packages, you must tell the `mojo-extension` code where
the root packages are that need to be searched for extension factories.  Then what we
do is we register the root modules under which the factory types will be found.

---------------------------------------------------------------
Setting the MJR_CONFIGURED_FACTORY_MODULES Variable from Python
---------------------------------------------------------------

.. code:: python

    from mojo.extension.extensionconfiguration import ExtensionConfiguration
    from mojo.extension.wellknown import ConfiguredSuperFactorySingleton

    ExtensionConfiguration.MJR_CONFIGURED_FACTORY_MODULES = [
            "mypkg.factories",
        ]

---------------------------------------------------------------
Setting the MJR_CONFIGURED_FACTORY_MODULES Environment Variable
---------------------------------------------------------------

.. code::
    
    MJR_CONFIGURED_FACTORY_MODULES=mypkg.a.factories,mypkg.b.factories

----------------------------------------------------------------
Setting the MJR_CONFIGURED_FACTORY_MODULES in the Startup Config
----------------------------------------------------------------

.. code::
    
    [MOJO-EXTENSION]
    MJR_CONFIGURED_FACTORY_MODULES=mypkg.a.factories,mypkg.b.factories

========================
Loading Custom Factories
========================

In order to load extension factories, we utilize the `ConfiguredSuperFactorySingleton` singleton
object that is maintained by the `mojo-extension` package.  You can get a reference to the super
factory singleton by using code similar to the code below:

.. code:: python

    from mojo.extension.wellknown import ConfiguredSuperFactorySingleton

    superfactory = ConfiguredSuperFactorySingleton()


Then when we want to get the type from the extension, we utilize the protocol that
was declared and ask for the type using the function on the protocol that will return
the type.

.. code:: python

    hey_type = self._super_factory.get_override_types_by_order(MyExtTypeProtocol.give_me_a_hey)
    ho_type = self._super_factory.get_override_types_by_order(MyExtTypeProtocol.give_me_a_ho)

    hey = hey_type()
    ho = ho_type()

    print("")
    print(f"{hey}... {ho}... {hey}... {ho}...")


==========
References
==========

- `User Guide <userguide/userguide.rst>`_
- `Coding Standards <userguide/10-00-coding-standards.rst>`_
