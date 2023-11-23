=================================
Automation Mojo Extension Package
=================================

This is a python package that provides a mechanism for extending other python packages.  This
package is different from other python extension packages in that it uses the python Protocol type
to query for a type.

For example, if we want to be able to create instance of object like these from a factory.

.. code:: python

    class Hey:
        def __str__(self):
            return "Hey"

    class Ho:
        def __str__(self):
            return "Ho"


    class MyExtTypeProtocol(ExtProtocol):

        ext_protocol_name = "mojo-myextypeprotocol"

        @classmethod
        def give_me_a_hey(cls):
            ...

        @classmethod
        def give_me_a_ho(cls):
            ...

    class MyExtTypeFactory(ExtFactory, MyExtTypeProtocol):

        @classmethod
        def give_me_a_hey(cls):
            return Hey
        
        @classmethod
        def give_me_a_ho(cls):
            return Ho


Then what we do i we register the module where the type is found.

.. code:: python

    from mojo.extension.extensionconfiguration import ExtensionConfiguration
    from mojo.extension.wellknown import ConfiguredSuperFactorySingleton

    ExtensionConfiguration.CONFIGURED_FACTORY_MODULES = [
            "myextinst",
            "myexttype"
        ]


Then we get an instance of the super factory singleton.

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
