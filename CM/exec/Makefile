#
# ===== Build options begin here =====
#

#
# Specify the C++ compiler.  This is also used for linking the executable.
#

#CXX = g++
#FC = gfortran

#CXX = icc
#FC = ifort
#
# Specify compiler options (optimization level, debugging options, etc.)
#

CXXFLAGS = -O3 # -g

#
# Specify the location of the BLAS and LAPACK libraries.  Depending upon the
# directories searched by the linker by default, it may not be necessary to
# specify these, in which case they can be left undefined (empty).  You can first
# try building with these macros undefined (empty) to find out.  If the libraries
# aren't found, or if a specific implementation of BLAS/LAPACK located elsewhere
# is desired, set these macros to the location of libblas.a and liblapack.a,
# respectively.
#

LAPACK_LOC =
BLAS_LOC =

#
# The M-tree database can be read/written from/to a file in HDF5 format, but
# this is optional.  If such functionality is desired, then specify the location
# of the HDF5 library (i.e., the top level directory containing the bin, include
# and lib subdirectories).  Otherwise just leave this macro undefined (empty).
#

HDF5_LOC =
HDF5_DEFINES = -DH5_USE_16_API

#
# ===== Build options end here =====
#


FORTRAN_LIBS= -lifcore
LIBS = -lm

ifneq ($(strip $(LAPACK_LOC)),)
LIBS += -L$(LAPACK_LOC)
endif
LIBS += -llapack

ifneq ($(strip $(BLAS_LOC)),)
LIBS += -L$(BLAS_LOC)
endif
LIBS += -lblas

ifeq ($(strip $(HDF5_LOC)),)
CXXFLAGS += -UHAVE_PKG_hdf5
else
CXXFLAGS += -DHAVE_PKG_hdf5 -I$(HDF5_LOC)/include $(HDF5_DEFINES)
LIBS += -L$(HDF5_LOC)/lib -lhdf5
endif

# Tensors

TENSOR_LOC  = ../src/tensors
TENSOR_SRC  = $(TENSOR_LOC)/tensor.cc $(TENSOR_LOC)/xtensor.cc $(TENSOR_LOC)/tutils.cc
TENSOR_INCL = $(TENSOR_SRC:.cc=.h)
TENSOR_OBJS = $(TENSOR_SRC:.cc=.o)
TENSOR_DEPS = $(TENSOR_SRC:.cc=.d)

# Adaptive sampling

AS_LOC        = ../src/adaptive_sampling
INTERPDB_LOC  = $(AS_LOC)/interpolation_database
INTERPDB_SRC  = $(shell ls $(INTERPDB_LOC)/base/*.cc $(INTERPDB_LOC)/kriging_database/*.cc)
INTERPDB_INCL = $(shell ls $(INTERPDB_LOC)/kriging_database/*.h $(INTERPDB_LOC)/base/*.h $(INTERPDB_LOC)/base/*.I)
INTERP_LOC    = $(AS_LOC)/interpolation
INTERP_SRC    = $(shell ls $(INTERP_LOC)/*/*.cc)
INTERP_INCL   = $(shell ls $(INTERP_LOC)/base/*.h $(INTERP_LOC)/base/*.I)
DB_LOC        = $(AS_LOC)/database
DB_SRC        = $(shell ls $(DB_LOC)/mtreedb/*.cc)
DB_INCL       = $(shell ls $(DB_LOC)/mtreedb/*.h $(DB_LOC)/mtreedb/*.I)
UTILS_LOC     = $(AS_LOC)/utils
UTILS_SRC     = $(shell ls $(UTILS_LOC)/toolbox/*/*.cc $(UTILS_LOC)/murmur3/*.cc)
UTILS_INCL    = $(shell ls $(UTILS_LOC)/toolbox/base/*.h $(UTILS_LOC)/toolbox/base/*.I $(UTILS_LOC)/toolbox/database/*.h $(UTILS_LOC)/toolbox/database/*.I $(UTILS_LOC)/toolbox/stream/*.h $(UTILS_LOC)/toolbox/stream/*.I $(UTILS_LOC)/murmur3/*.h)
MTL_LOC       = $(AS_LOC)/mtl_headers
MTL_INCL      = $(shell ls $(AS_LOC)/mtl_headers/mtl/*.h)
AS_SRC        = $(AS_LOC)/AdaptiveSampler.cc $(INTERPDB_SRC) $(INTERP_SRC) $(DB_SRC) $(UTILS_SRC)
AS_OBJS       = $(AS_SRC:.cc=.o)
AS_DEPS       = $(AS_SRC:.cc=.d)
AS_LOC        = ../src/adaptive_sampling
AS_INCL       = $(shell ls $(AS_LOC)/*.h)

# Constitutive models

CM_LOC   = ../src/constitutive_models
CM_SRC   = $(shell ls $(CM_LOC)/*.cc)
CM_INCL  = $(CM_SRC:.cc=.h)
CM_OBJS  = $(CM_SRC:.cc=.o)
CM_DEPS  = $(CM_SRC:.cc=.d)

# EOS models

EOS_LOC  = ../src/eos_models
EOS_SRC  = $(shell ls $(EOS_LOC)/*.cc)
EOS_INCL = $(EOS_SRC:.cc=.h) $(EOS_LOC)/EOS.h
EOS_OBJS = $(EOS_SRC:.cc=.o)
EOS_DEPS = $(EOS_SRC:.cc=.d)

# Fine scale models

FS_LOC  = ../src/fine_scale_models
FS_F_LOC  = ../src/fine_scale_models/fortran
FS_SRC  = $(shell ls $(FS_LOC)/*.cc)
FS_INCL = $(FS_SRC:.cc=.h) $(FS_LOC)/FineScale.h
FS_OBJS = $(FS_SRC:.cc=.o)
FS_F_SRC  = $(shell ls $(FS_F_LOC)/*.f90)
FS_F_OBJS = $(shell ls $(FS_F_LOC)/*.o)
#FS_F_OBJS = init.o  libraryR8.o  vpEtxt_interface_base.o  vpscVpETxt_interface.o  vpsc_as_N2O.o TaylorFort.o
FS_DEPS = $(FS_SRC:.cc=.d) ${FS_F_SRC:.f90=.d}

# Standalone kinematic system test

KINTEST_OBJS = kintest.o $(CM_OBJS) $(EOS_OBJS) $(FS_OBJS) $(AS_OBJS) $(TENSOR_OBJS)
KINTEST_DEPS = kintest.d

# Standalone kinematic system test

MODTEST_OBJS = modtest.o $(CM_OBJS) $(EOS_OBJS) $(FS_OBJS) $(AS_OBJS) $(TENSOR_OBJS)
MODTEST_F_OBJS = ${FS_F_OBJS}
MODTEST_DEPS = modtest.d

# Constitutive model library

CMLIB_SRC  = $(CM_SRC) $(EOS_SRC) $(FS_SRC) $(AS_SRC) $(TENSOR_SRC)
CMLIB_OBJS = $(CM_OBJS) $(EOS_OBJS) $(FS_OBJS) $(AS_OBJS) $(TENSOR_OBJS) ${FS_F_OBJS}
CMLIB_INCL = $(INTERPDB_INCL) $(DB_INCL) $(UTILS_INCL) $(CM_INCL) $(EOS_INCL) $(FS_INCL) $(TENSOR_INCL) $(INTERP_INCL) $(AS_INCL)

CXXFLAGS += -std=c++11
CXXFLAGS += -I$(AS_LOC) -I$(MTL_LOC) -I$(INTERPDB_LOC) -I$(INTERPDB_LOC)/kriging_database -I$(INTERPDB_LOC)/base -I$(INTERP_LOC) -I$(INTERP_LOC)/base
CXXFLAGS += -I$(DB_LOC) -I$(DB_LOC)/mtreedb -I$(UTILS_LOC) -I$(UTILS_LOC)/toolbox/base
CXXFLAGS += -I$(UTILS_LOC)/toolbox/database -I$(UTILS_LOC)/toolbox/stream
CXXFLAGS += -I$(TENSOR_LOC) -I$(CM_LOC) -I$(EOS_LOC) -I$(FS_LOC)
CXXFLAGS += -DDBL_SNAN_IS_BROKEN -DFLT_SNAN_IS_BROKEN

ifeq ($(REDIS), yes)
REDIS_LOC = ../../redis/hiredis
REDIS_SERVER = $(realpath ../../redis/redis/src/redis-server)
CXXFLAGS += -DREDIS -I$(REDIS_LOC) -DREDIS_SERVER=\"${REDIS_SERVER}\"
REDIS_LIBS = $(REDIS_LOC)/libhiredis.a
endif

ifeq ($(FLANN), yes)
FLANN_LOC = ../../flann/flann/src/cpp
CXXFLAGS += -DFLANN -I$(FLANN_LOC)
endif

ifeq ($(HIO), yes)
CXXFLAGS += -DHIO -I$(LIBHIO_INCLUDE) 
HIO_LIBS = $(LIBHIO_INCLUDE)/../lib/libhio.a
endif

ifeq ($(TWEMPROXY), yes)
TWEMPROXY_SERVER = $(realpath ../../twemproxy/twemproxy-master/src/nutcracker)
CXXFLAGS += -DNUTCRACKER_SERVER=\"${TWEMPROXY_SERVER}\"
endif

# LOGGER depends on REDIS=yes
# IF REDIS=no, logging ends up being a NO OP
ifeq ($(LOGGER)$(REDIS), yesyes)
LOGGER_LOC = ../../logger
LOGGER_LIBS = $(LOGGER_LOC)/liblogger.a
CXXFLAGS += -DLOGGER -I$(LOGGER_LOC)
endif

ifeq ($(FSTRACE), yes)
CXXFLAGS += -DFSTRACE
endif

OPTFLAGS = $(CXXFLAGS) $(CCFLAGS)

MAKEDEPEND = $(CC) -MM -MT $*.o $(CXXFLAGS) -o $*.d.tmp $<

default: libcm

libcm: ../lib/libcm.a

kintest: $(KINTEST_OBJS)
	$(CXX) $(CXXFLAGS) $(KINTEST_OBJS) $(LIBS) $(FORTRAN_LIBS) -o kintest

modtest: $(MODTEST_OBJS) ${MODTEST_F_OBJS}
	${FC} -c ${FS_F_SRC}
	$(CXX) $(CXXFLAGS) $(MODTEST_OBJS) ${MODTEST_F_OBJS} $(LIBS) $(FORTRAN_LIBS) -o modtest 

dummy: ;

.cxxflags: dummy
	@[ -f $@ ] || touch $@
	@echo "CXXFLAGS=$(CXXFLAGS)" | cmp -s $@ - || echo "CXXFLAGS=$(CXXFLAGS)" > $@

../lib/libcm.a:  $(CMLIB_OBJS) $(REDIS_LIBS)  $(HIO_LIBS) $(LOGGER_LIBS)
	ar crsT libcm.a $(CMLIB_OBJS) $(REDIS_LIBS)  $(HIO_LIBS) $(LOGGER_LIBS)
	cp $(CMLIB_INCL) ../include
	mkdir -p ../include/mtl
	cp $(MTL_INCL) ../include/mtl
	mv libcm.a ../lib

%.o : %.cc .cxxflags
	@$(MAKEDEPEND)
	cp $*.d.tmp $*.d
	sed -e 's/#.*//' -e 's/^[^:]*: *//' -e 's/ *\\$$//' -e '/^$$/ d' -e 's/$$/ :/' < $*.d.tmp >> $*.d
	rm -f $*.d.tmp
	$(CXX) -c $(OPTFLAGS)  -c -o $@ $< 

-include $(CM_DEPS)
-include $(AS_DEPS)
-include $(FS_DEPS)
-include $(TENSOR_DEPS)
-include $(EOS_DEPS)
-include $(KINTEST_DEPS)

clean:
	$(RM) $(AS_OBJS) $(AS_DEPS) $(CM_OBJS) $(CM_DEPS) $(FS_OBJS) $(FS_DEPS)
	$(RM) $(TENSOR_OBJS) $(TENSOR_DEPS) $(EOS_OBJS) $(EOS_DEPS) $(KINTEST_OBJS) $(KINTEST_DEPS) *.a

realclean: clean
	$(RM) -r kintest ../include/* ../lib/*


