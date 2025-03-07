import periodictable
from periodictable.constants import neutron_mass

def test():
    # Constants defined in the tables. These may be updated from time to time.
    Be_12_mass = 12.0269221
    Be_mass = 9.012182
    Pb_206_abundance = 24.1
    Pb_209_abundance = 0
    Pb_mass = 207.2

    assert periodictable.Be[12].mass == Be_12_mass
    assert periodictable.Be.mass == Be_mass
    assert abs(periodictable.Be[12].ion[2].mass - (Be_12_mass - 2*periodictable.constants.electron_mass))<1e-12
    assert abs(periodictable.Be.ion[2].mass - (Be_mass - 2*periodictable.constants.electron_mass))<1e-12
    assert periodictable.Pb[206].abundance == Pb_206_abundance
    assert periodictable.Pb[209].abundance == Pb_209_abundance
    assert periodictable.Pb.mass == Pb_mass
    assert periodictable.n.mass == neutron_mass

    # Check abundance totals to 0% or 100%
    for el in periodictable.elements:
        abundance=0
        for iso in el:
            if iso.abundance == None:
                print("%s abundance=None"%iso)
            else:
                abundance += iso.abundance
        assert abs(abundance-100) < 1e-4 or abundance==0,\
            "total abundance for %s is %.15g%%"%(el.symbol,abundance)


    # Check average mass corresponds to abundance information
    # Note: should check that this is true within uncertainty, but
    # uncertainties are not being loaded.
    for el in periodictable.elements:
        abundance=0
        mass=0
        for iso in el:
            if iso.abundance == None:
                print("%s abundance=None"%iso)
            else:
                abundance += iso.abundance
                mass += iso.mass*iso.abundance/100.
        assert abundance==0 or abs(mass - el.mass)/el.mass  < 1e-3,\
            "avg mass for %s is %g != %g"%(el.symbol,el.mass,mass)


if __name__ == "__main__": test()
