************************
Christmas Labels Program
************************


Purpose
=======

This program will manage an organized list of people so that address labels
can be printed and used to mail Christmas cards or other purposes.

Content
#######

The list of people will consist of entries containing names, addresses and
certain indicators.

Names
-----

Each entry will track one or two people who are living together.  The first
field will have the first line of how the label will be addressed.  Examples
are:

    -   Mr. and Mrs. Adam Smith
    -   Rev. and Mr. Eve Pastor
    -   Mr. John and Dr. Jones
    -   Ms. Janice and Ms. Alisa Saunders

The field will be up to 30 characters wide and will not be formatted.

Another field will be available to specify sort order.  This field will not be
printed but will be one of the ways labels can be printed.  (See `Label
Printing`_ below.

Addresses
---------

One or two addresses will be maintained per entry.  Each address will
consist of one or two lines of street address, as well as a city, state, and
postal code.  Thus up to three lines can be specified per address.  Each
line will be no more than 30 characters wide.

Indicators
----------

One indicator will be maintained per entry to designate if this entry is to
be printed or not.

Another indicator will be maintained per entry that will designate which of
the two entries is to be used for the label at the time of printing.

    At this time, no attempt to automate the address chosen by date or other
    means will be incorporated in the program.

Printing Output
###############

Label Printing
--------------

A single label format will be targeted by this program.  It is the common
thirty labels per 8 1/2" by 11" sheet (three across by ten down) found in
many office supply stores in the United States.

Labels can be printed in one of two orders:

    -   Sort order only (see `Names`_ above)
    -   Postal code then sort order.

(If sort order is not unique across entries, the order of labels printed in
indeterminate.)

Labels will be printed top to bottom and left to right.

Other Printed Output
--------------------

No other printed output is planned at this time.  (However, the program will
not know whether labels or plain paper is in the printer.)


Import and Export Files
#######################

This program will also allow data to be imported and exported via CSV-like
files.  Since commas are very likely to be included in addresses, the file
will use tabs to delimit fields rather than commas.  Also, any  new
lines imbedded in the fields in the import file will be removed.

Primary Interface
#################

The primary interface will be a standalone python program with a GUI
interface.  The GUI will be using wxPython designed using Glade.  See the
UML diagrams for the details.

Data Repository
###############

The data for the names, addresses, etc. will be stored in a database.  Since
the targeted user has no IT experience, the data will be stored in a Sqlite
database since it does not require a server or other overhead.
