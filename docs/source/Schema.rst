***************
Database Schema
***************

There are several tables for this solution.  The primary table is a list of
contacts.

Table Definitions
=================

Contacts Table
--------------

Contains the names and addresses of the people who are to get Christmas cards.

Contacts Field Definitions
--------------------------

============   =========   ====    =====================  ===================
Name           Type        Size    Attributes             Comments
============   =========   ====    =====================  ===================
ContactID      Sequence    Int     Auto-assigned, Unique  Intenal use only
NameLine       Text        30                             Used for both
PrintLabel     Boolean     Bool    Values: Yes, No        Should label print?
WhichAddress   Boolean     Bool    Values: Home, Away     Which address to use
HomeStreet     Text        30
HomeCity       Text        19
HomeState      Text        2
HomeZip        Text        6
AwayStreet     Text        30
AwayCity       Text        19
AwayState      Text        2
AwayZip        Text        6
SortName       Text        20                             Last name sort
============   =========   ====    =====================  ===================


State Table
-----------

Contains the list of valid state or province codes and names

State Field Definitions
-----------------------

============   =========   ====    =====================  ===================
Name           Type        Size    Attributes             Comments
============   =========   ====    =====================  ===================
StateID        Sequence    Int     Auto-assigned, Unique  Intenal use only
StateCode      Text        2                              May be a province
StateName      Text        30                             Added as needed
============   =========   ====    =====================  ===================

