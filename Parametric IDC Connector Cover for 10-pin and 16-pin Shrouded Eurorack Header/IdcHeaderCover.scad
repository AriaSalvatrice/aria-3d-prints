// 5 for 10-pin, 8 for 16-pin, etc
PinsPerCol = 5; 

width = 5.0 + PinsPerCol * 2.54;

// Pins are 1mm, make it larger for better fit
PinSize = 1.6;

module mainConnector() {
    difference(){
        cube([width, 6.5, 9]);
        for (i = [ 0 : PinsPerCol - 1] ){
            union() {
                translate([i * 2.54 + 3.8, 1.73, 0]) {
                    cylinder(h = 17, r = PinSize / 2, center = true, $fn=20);
                }
                translate([i * 2.54 + 3.8, 4.27, 0]) {
                    cylinder(h = 17, r = PinSize / 2, center = true, $fn=20);
                }
            }
        }
    }
}

module handle() {
    union() {
        linear_extrude(height=3, scale=0.88) {
            square([width, 6.5], center= true);
        }
        
    }
}

union() {
    mainConnector();
    translate([width / 2, 3.25, 9]) {
        handle();
    }
    translate([width / 2, 3.25, 15]) {
        rotate([180, 0, 0]) {
            handle();
        }
    }
    translate([width / 2 - 2,-2,0]) {
        cube([4, 2, 9]);
    }
}
