#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "papi.h"
#define NUM_EVENTS 8

//Michael Thorman
//Lab2
//CSCI490/Fall 2021
//9/23/2021

//low level API
int Events[NUM_EVENTS]= {PAPI_TOT_CYC,PAPI_TOT_INS, PAPI_L1_DCM, PAPI_L1_ICM, PAPI_L2_DCM, PAPI_L2_ICM, PAPI_TLB_DM, PAPI_TLB_IM}; //PAPI events
int EventSet = PAPI_NULL;
long long values[NUM_EVENTS];

void ijk(double *A, double *B, double *C, int n){
int i, j, k;
double sum;
int retval;
long long start_cycles, end_cycles, start_usec, end_usec;

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(A+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(B+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }
}

retval = PAPI_library_init (PAPI_VER_CURRENT); //initializing library
retval = PAPI_create_eventset(&EventSet); //allocating space for the new eventset and do setup
retval = PAPI_add_events(EventSet, Events, NUM_EVENTS); //add flops and total cycles to the eventset
start_cycles = PAPI_get_real_cyc(); //gets the starting time in clock cycles
start_usec = PAPI_get_real_usec(); //gets the starting time in microseconds
retval = PAPI_start(EventSet); //start the counters

for(i=0; i<n; i++){
    for(j=0; j<n; j++){
        sum =0.0;
        for(k=0; k<n; k++){
            sum = sum + A[i*n+k]*B[k*n+j];
            C[i*n+j]=sum;
        }
    }
}
retval=PAPI_stop(EventSet, values); //stop counters and store results in values
end_cycles=PAPI_get_real_cyc(); //gets the ending time in clock cycles
end_usec=PAPI_get_real_usec(); //gets the ending time in microseconds
printf("=====================================================================\n");
printf("IJK Results (N=500): \n");
printf("PAPI_TOT_CYC/Total Cycles: %lld\n", values[0]);
printf("PAPI_TOT_INS/Instructions completed: %lld\n", values[1]);
printf("Wall clock cycles: %lld\n", end_cycles-start_cycles);
printf("Wall clock time in microseconds: %lld\n", end_usec-start_usec);
printf("PAPI_L1_DCM/Level 1 Data Cache Misses: %lld\n", values[2]);
printf("PAPI_L1_ICM/Level 1 Instruction Cache Misses: %lld\n", values[3]);
printf("PAPI_L2_DCM/Level 2 Data Cache Misses: %lld\n", values[4]);
printf("PAPI_L2_ICM/Level 2 Instruction Cache Misses: %lld\n", values[5]);
printf("PAPI_TLB_DM/Data translation lookaside buffer misses: %lld\n", values[6]);
printf("PAPI_TLB_IM/Instruction translation lookaside buffer misses: %lld\n", values[7]);
printf("=====================================================================\n");
}


void jik(double *A, double *B, double *C, int n){
int i, j, k;
double sum;
int retval;
long long start_cycles, end_cycles, start_usec, end_usec;

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(A+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(B+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

retval = PAPI_library_init (PAPI_VER_CURRENT);
retval = PAPI_create_eventset(&EventSet);
retval = PAPI_add_events(EventSet, Events, NUM_EVENTS);
start_cycles = PAPI_get_real_cyc();
start_usec = PAPI_get_real_usec();
retval = PAPI_start(EventSet);

for(j=0; j<n; j++){
    for(i=0; i<n; i++){
        sum =0.0;
        for(k=0; k<n; k++){
            sum = sum + A[i*n+k]*B[k*n+j];
            C[i*n+j]=sum;
        }
    }
}
retval=PAPI_stop(EventSet, values);
end_cycles=PAPI_get_real_cyc();
end_usec=PAPI_get_real_usec();
printf("=====================================================================\n");
printf("JIK Results (N=500): \n");
printf("PAPI_TOT_CYC/Total Cycles: %lld\n", values[0]);
printf("PAPI_TOT_INS/Instructions completed: %lld\n", values[1]);
printf("Wall clock cycles: %lld\n", end_cycles-start_cycles);
printf("Wall clock time in microseconds: %lld\n", end_usec-start_usec);
printf("PAPI_L1_DCM/Level 1 Data Cache Misses: %lld\n", values[2]);
printf("PAPI_L1_ICM/Level 1 Instruction Cache Misses: %lld\n", values[3]);
printf("PAPI_L2_DCM/Level 2 Data Cache Misses: %lld\n", values[4]);
printf("PAPI_L2_ICM/Level 2 Instruction Cache Misses: %lld\n", values[5]);
printf("PAPI_TLB_DM/Data translation lookaside buffer misses: %lld\n", values[6]);
printf("PAPI_TLB_IM/Instruction translation lookaside buffer misses: %lld\n", values[7]);
printf("=====================================================================\n");

}

void kij(double *A, double *B, double *C, int n){
int i, j, k;
double sum, r;
int retval;
long long start_cycles, end_cycles, start_usec, end_usec;
for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(A+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(B+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}
retval = PAPI_library_init (PAPI_VER_CURRENT);
retval = PAPI_create_eventset(&EventSet);
retval = PAPI_add_events(EventSet, Events, NUM_EVENTS);
start_cycles = PAPI_get_real_cyc();
start_usec = PAPI_get_real_usec();
retval = PAPI_start(EventSet);
for(k=0; k<n; k++){
    for(i=0; i<n; i++){
        r =A[i*n+k];
        for(j=0; j<n; j++){
            C[i*n+j] = C[i*n+j] + r*B[k*n+j];
        }
    }
}
retval=PAPI_stop(EventSet, values);
end_cycles=PAPI_get_real_cyc();
end_usec=PAPI_get_real_usec();
printf("=====================================================================\n");
printf("KIJ Results (N=500): \n");
printf("PAPI_TOT_CYC/Total Cycles: %lld\n", values[0]);
printf("PAPI_TOT_INS/Instructions completed: %lld\n", values[1]);
printf("Wall clock cycles: %lld\n", end_cycles-start_cycles);
printf("Wall clock time in microseconds: %lld\n", end_usec-start_usec);
printf("PAPI_L1_DCM/Level 1 Data Cache Misses: %lld\n", values[2]);
printf("PAPI_L1_ICM/Level 1 Instruction Cache Misses: %lld\n", values[3]);
printf("PAPI_L2_DCM/Level 2 Data Cache Misses: %lld\n", values[4]);
printf("PAPI_L2_ICM/Level 2 Instruction Cache Misses: %lld\n", values[5]);
printf("PAPI_TLB_DM/Data translation lookaside buffer misses: %lld\n", values[6]);
printf("PAPI_TLB_IM/Instruction translation lookaside buffer misses: %lld\n", values[7]);
printf("=====================================================================\n");

}

void ikj(double *A, double *B, double *C, int n){
int i, j, k;
double sum, r;
int retval;
long long start_cycles, end_cycles, start_usec, end_usec;

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(A+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(B+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

retval = PAPI_library_init (PAPI_VER_CURRENT);
retval = PAPI_create_eventset(&EventSet);
retval = PAPI_add_events(EventSet, Events, NUM_EVENTS);
start_cycles = PAPI_get_real_cyc();
start_usec = PAPI_get_real_usec();
retval = PAPI_start(EventSet);
for(i=0; i<n; i++){
    for(k=0; k<n; k++){
        r =A[i*n+k];
        for(j=0; j<n; j++){
            C[i*n+j] = C[i*n+j] + r*B[k*n+j];
        }
    }
}
retval=PAPI_stop(EventSet, values);
end_cycles=PAPI_get_real_cyc();
end_usec=PAPI_get_real_usec();
printf("=====================================================================\n");
printf("IKJ Results (N=500): \n");
printf("PAPI_TOT_CYC/Total Cycles: %lld\n", values[0]);
printf("PAPI_TOT_INS/Instructions completed: %lld\n", values[1]);
printf("Wall clock cycles: %lld\n", end_cycles-start_cycles);
printf("Wall clock time in microseconds: %lld\n", end_usec-start_usec);
printf("PAPI_L1_DCM/Level 1 Data Cache Misses: %lld\n", values[2]);
printf("PAPI_L1_ICM/Level 1 Instruction Cache Misses: %lld\n", values[3]);
printf("PAPI_L2_DCM/Level 2 Data Cache Misses: %lld\n", values[4]);
printf("PAPI_L2_ICM/Level 2 Instruction Cache Misses: %lld\n", values[5]);
printf("PAPI_TLB_DM/Data translation lookaside buffer misses: %lld\n", values[6]);
printf("PAPI_TLB_IM/Instruction translation lookaside buffer misses: %lld\n", values[7]);
printf("=====================================================================\n");
}

void jki(double *A, double *B, double *C, int n){
int i, j, k;
double r;
long long start_cycles, end_cycles, start_usec, end_usec;
int retval;
for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(A+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(B+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

retval = PAPI_library_init (PAPI_VER_CURRENT);
retval = PAPI_create_eventset(&EventSet);
retval = PAPI_add_events(EventSet, Events, NUM_EVENTS);
start_cycles = PAPI_get_real_cyc();
start_usec = PAPI_get_real_usec();
retval = PAPI_start(EventSet);
for(j=0; j<n; j++){
    for(k=0; k<n; k++){
        r =B[k*n+j];
        for(i=0; i<n; i++){
            C[i*n+j] = C[i*n+j] + A[i*n+k]*r;
        }
    }
}
retval=PAPI_stop(EventSet, values);
end_cycles=PAPI_get_real_cyc();
end_usec=PAPI_get_real_usec();
printf("=====================================================================\n");
printf("JKI Results (N=500): \n");
printf("PAPI_TOT_CYC/Total Cycles: %lld\n", values[0]);
printf("PAPI_TOT_INS/Instructions completed: %lld\n", values[1]);
printf("Wall clock cycles: %lld\n", end_cycles-start_cycles);
printf("Wall clock time in microseconds: %lld\n", end_usec-start_usec);
printf("PAPI_L1_DCM/Level 1 Data Cache Misses: %lld\n", values[2]);
printf("PAPI_L1_ICM/Level 1 Instruction Cache Misses: %lld\n", values[3]);
printf("PAPI_L2_DCM/Level 2 Data Cache Misses: %lld\n", values[4]);
printf("PAPI_L2_ICM/Level 2 Instruction Cache Misses: %lld\n", values[5]);
printf("PAPI_TLB_DM/Data translation lookaside buffer misses: %lld\n", values[6]);
printf("PAPI_TLB_IM/Instruction translation lookaside buffer misses: %lld\n", values[7]);
printf("=====================================================================\n");

}
void kji(double *A, double *B, double *C, int n){
int i, j, k;
double r;
long long start_cycles, end_cycles, start_usec, end_usec;
int retval;
for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(A+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

for (i=0; i<n; i++){
    for(j=0; j<n; j++){
        *(B+i*n+j)=((double)rand()*(10-1))/((double)RAND_MAX)+1;
    }

}

retval = PAPI_library_init (PAPI_VER_CURRENT);
retval = PAPI_create_eventset(&EventSet);
retval = PAPI_add_events(EventSet, Events, NUM_EVENTS);
start_cycles = PAPI_get_real_cyc();
start_usec = PAPI_get_real_usec();
retval = PAPI_start(EventSet);
for(k=0; k<n; k++){
    for(j=0; j<n; j++){
        r =B[k*n+j];
        for(i=0; i<n; i++){
            C[i*n+j] = C[i*n+j] + A[i*n+k]*r;
        }
    }
}
retval=PAPI_stop(EventSet, values);
end_cycles=PAPI_get_real_cyc();
end_usec=PAPI_get_real_usec();
printf("=====================================================================\n");
printf("KJI Results (N=500): \n");
printf("PAPI_TOT_CYC/Total Cycles: %lld\n", values[0]);
printf("PAPI_TOT_INS/Instructions completed: %lld\n", values[1]);
printf("Wall clock cycles: %lld\n", end_cycles-start_cycles);
printf("Wall clock time in microseconds: %lld\n", end_usec-start_usec);
printf("PAPI_L1_DCM/Level 1 Data Cache Misses: %lld\n", values[2]);
printf("PAPI_L1_ICM/Level 1 Instruction Cache Misses: %lld\n", values[3]);
printf("PAPI_L2_DCM/Level 2 Data Cache Misses: %lld\n", values[4]);
printf("PAPI_L2_ICM/Level 2 Instruction Cache Misses: %lld\n", values[5]);
printf("PAPI_TLB_DM/Data translation lookaside buffer misses: %lld\n", values[6]);
printf("PAPI_TLB_IM/Instruction translation lookaside buffer misses: %lld\n", values[7]);
printf("=====================================================================\n");

}

int main()
{
int n;
printf("Please enter a value for N: ");
scanf("%d", &n);
//allocating space dynamically for large N arrays
double (*A)[n]=malloc(sizeof(double[n][n]));
double (*B)[n]=malloc(sizeof(double[n][n]));
double (*C)[n]=malloc(sizeof(double[n][n]));
//calling functions to test each individual matrix multiplication algorithm
//ijk(A[0], B[0], C[0], n);
//jik(A[0], B[0], C[0], n);
//kij(A[0], B[0], C[0], n);
ikj(A[0], B[0], C[0], n);
//jki(A[0], B[0], C[0], n);
//kji(A[0], B[0], C[0], n);
//freeing allocated memory
free(A);
free(B);
free(C);


return 0;
}

