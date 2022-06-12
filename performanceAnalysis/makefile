##Michael Thorman
##Lab2
##CSCI490/Fall 2021
##9/23/2021

## Compiler, tools and options
FC = ftn
CC = cc
LINK = cc

PAPI_ROOT  = /opt/cray/pe/papi/6.0.0.7
INC = -I $(PAPI_ROOT)/include

OPT = -rdynamic
ADDCFLAGS = -Wall
CCFLAGS = $(OPT)

## Files
OBJECTS = main.o
TARGET = main
LIBS = -L $(PAPI_ROOT)/lib -lpapi

##Implicit Rules
.SUFFIXES:.c
.c.o:
	$(CC) -c $(CCFLAGS) $(ADDCFLAGS) $(INC) $<

.f.o:
	$(FC) -c $(CCFLAGS) $(INC) $<

##Build rules
all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(LINK) -o $@ $(OBJECTS) $(LDFLAGS) $(LIBS)

clean:
	rm -f $(OBJECTS) $(TARGET)
	rm -f*~core


