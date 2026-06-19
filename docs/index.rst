ibflex
======

Parse Interactive Brokers Flex Query XML statements into typed Python objects.
The library converts each Flex report element into a typed dataclass, casting
fields to native Python types (dates, decimals, enums), and can optionally
download statements directly from the IBKR Flex Web Service.

.. toctree::
   :maxdepth: 2
   :caption: API reference

   client
   enums
   parser
   Types
   utils

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
