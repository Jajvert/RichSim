#include "OPTICKS_LOG.hh"
#include "SimulationCore.hh"

int main( int argc, char** argv )
{
    OPTICKS_LOG( argc, argv );

    SimulationCore rich;
    rich.beamOn(1);

    return 0;
}
