#include <stdio.h>
#include <math.h>
#include <string.h>
#include <strings.h>
#include <time.h>
#include <assert.h>

#define STR_MAX 10000
const long double dt = 10;
const int PER_DAY = 1;

const long double G = 6.67430e-11 / 1e9;

typedef struct {
    long double x;
    long double y;
    long double z;
} vect;

typedef struct {
    char name[10];
    vect pos, vel;
    long double mass;
} Planet;

void update_pos(Planet planets[], int n);


long double mag(vect a) {
    return sqrt((double) (a.x * a.x + a.y * a.y + a.z * a.z));
}

long double sqr_mag(vect a) {
    return (a.x * a.x + a.y * a.y + a.z * a.z);
}

vect add(vect a, vect b) {
    return (vect) { a.x + b.x, a.y + b.y, a.z + b.z };
}

vect scalar_mult(vect a, long double b) {
    return (vect) { a.x* b, a.y* b, a.z* b };
}

vect neg(vect a) {
    return (vect) { -a.x, -a.y, -a.z };
}

void jsonify(float time, Planet p[], int n, char s[]) {
    char log[STR_MAX] = "";
    sprintf(log, "\"%f\":{", time);
    strcat(s, log);
    for (int i = 0; i < n;i++) {
        sprintf(log, "\"%s\":{\"pos\":{\"x\":%Lf,\"y\":%Lf,\"z\":%Lf},\"vel\":{\"x\":%Lf,\"y\":%Lf,\"z\":%Lf},\"mass\":%Lf},", p[i].name, p[i].pos.x, p[i].pos.y, p[i].pos.z, p[i].vel.x, p[i].vel.y, p[i].vel.z, p[i].mass);
        strcat(s, log);
    }
    strcat(s, "},\n");
}

double get_time(clock_t *start) {
    clock_t curr_time = clock();
    double time_passed = (double) (curr_time - *start) / CLOCKS_PER_SEC;
    *start = curr_time;
    return time_passed;
}

int main() {
    clock_t start = clock();
    clock_t curr_time = start;

    FILE* fptr;
    fptr = fopen("solar_0_1.json", "w");
    fputs("{", fptr);

    //Origin in Solar System Baricenter, Frame of Reference is ICRF
    //Positions are in kilometers, velocities are in kilometers per second and mass is in kilograms
    /* Planet planets[] = {
        {
            .name = "Sun",
            .pos = {-1.218177533485452e6, -3.947657577842895e5,  3.169980087428029e4},
            .vel = {7.919103337676651E-03, -1.280510816612012E-02, -6.851824476021302E-05,},
            .mass = 1988500e24
        },
        {
            .name = "Mercury",
            .pos = {4.016655032109254e7, -4.741707138023977e7, -7.606990298084749e6},
            .vel = {2.689587527922549e1,  3.450258983454832e1,  3.542890309833879E-01},
            .mass = 3.302e23
        },
        {
            .name = "Venus",
            .pos = {-6.440334153946640e7,  8.641877036429313e7,  4.869778576070119e6},
            .vel = {-2.842688556343974e1, -2.081301439321888e1,  1.354986053594716e0},
            .mass = 48.685e23
        },
        {
            .name = "Earth",
            .pos = {6.785995976840912e7,  1.301432772789728e8,  2.395972772090882e4},
            .vel = {-2.679979312748531e1,  1.379780069910351e1, -1.817128036692317E-03},
            .mass = 5.97219e24
        },
        {
            .name = "Mars",
            .pos = {-1.197629918263210e8, -1.959573466258098e8, -1.158939467941597e6},
            .vel = {2.163912504043861e1, -1.049792136503175e1, -7.504043027066980E-01},
            .mass = 6.4171e23
        },
        {
            .name = "Jupiter",
            .pos = {.x = 5.507841514255924e8, .y = 4.993069601314266e8,.z = -1.439405967055380e7},
            .vel = {-8.921016786927400e0,  1.029916945707882e1,  1.568616655565376E-01},
            .mass = 189818.722e22
        },
        // {
        //     .name = "Saturn",
        //     .pos = {1.334224601955568E+09, -5.847124883065293E+08, -4.295531014713034E+07},
        //     .vel = {3.336412146214057E+00,  8.828256356694061E+00, -2.861970904310995E-01},
        //     .mass = 5.6834e26
        // },
        // {
        //     .name = "Uranus",
        //     .pos = {1.851618719493484e9,  2.275792905198487e9, -1.553574774653757e7},
        //     .vel = {-5.332547063420304e0,  3.980595912866628e0,  8.394288098242630e-2},
        //     .mass = 86.813e24
        // },
        // {
        //     .name = "Neptune",
        //     .pos = {4.462292465925602e9, -2.857958366478140e8, -9.695274844209039e7},
        //     .vel = {3.116027310608757E-01,  5.456607369163689e0, -1.194638155636847e-1},
        //     .mass = 102.409e24
        // },
        // {
        //     .name = "Pluto",
        //     .pos = {2.557804139665275e9, -4.543770281432278e9, -2.536597271372623e8},
        //     .vel = {4.864846883300995e0,  1.475365931076200e0, -1.547260275090102e0},
        //     .mass = 1.307e22
        // },

    }; */

    Planet planets[] = {
        {
            .name = "Earth",
            .pos = {.x = 147.10e9,.y = 0,.z = 0},
            .vel = {.x = 0,.y = 30.29e3,.z = 0},
            .mass = 5.97219e24
        },
        {
            .name = "Sun",
            .pos = {.x = 0,.y = 0,.z = 0},
            .vel = {.x = 0,.y = 0,.z = 0},
            .mass = 1.989e30
        },
    };


    printf("Elapsed time: %lfs\n", get_time(&curr_time));

    //normalise the origin to the sun, and velocities wrt to sun
    int n = (int) sizeof(planets) / sizeof(Planet);
    for (int i = 1; i < n; i++) {
        planets[i].pos = add(planets[i].pos, neg(planets[0].pos));
        planets[i].vel = add(planets[i].vel, neg(planets[0].vel));
    }
    planets[0].pos = (vect) {0, 0, 0};
    planets[0].vel = (vect) {0, 0, 0};

    // printf("%.12Lf %.12Lf %.12Lf\n", planets[0].pos.x, planets[0].pos.y, planets[0].pos.z);
    // printf("%.12Lf %.12Lf %.12Lf\n", planets[1].pos.x, planets[1].pos.y, planets[1].pos.z);

    printf("Elapsed time: %lfs\n", get_time(&curr_time));

    long days = 365 * 1;
    float t = 24.0f * 3600 / PER_DAY;
    long iterations = (long)(days * 24 * 3600 * (1 / dt));
    printf("Total iterations: %ld\n", iterations);

    int export_frequency = (int) (t / dt);
    float inv_secs_in_day = 1.0f / (24 * 3600);

    int j = 0;
    for (long i = 0; i < iterations; i++, j++) {
        update_pos(planets, n);
        if (j == export_frequency) {
            char s[STR_MAX] = "";
            jsonify(inv_secs_in_day, planets, n, s);
            fputs(s, fptr);
            j = 0;
        }
    }

    fputs("}", fptr);
    fclose(fptr);

    printf("Total time %.12lfs\n", get_time(&start));
}

void update_pos(Planet planets[], int n) {
    vect acc[n];

    //Calculate accelerations of planets assuming all planets are stationary
    for (int i = 0; i < n; i++) {
        acc[i] = (vect) {0, 0, 0};
    }

    for (int i = 0; i < n;i++) {
        Planet pi = planets[i];
        for (int j = 0; j < i;j++) {
            Planet pj = planets[j];
            vect dist = add(pj.pos, neg(pi.pos));
            // printf("%d %d %.12Lf\n", i, j, mag(dist));
            // printf("%.12Lf %.12Lf %.12Lf\n", pi.pos.x, pi.pos.y, pi.pos.z);
            // printf("%.12Lf %.12Lf %.12Lf\n", pj.pos.x, pj.pos.y, pj.pos.z);
            fflush(stdout);
            assert(mag(dist) != 0);
            vect aij = scalar_mult(dist, G * pj.mass / pow(mag(dist), 3));
            // if (i < 100)
            //     printf("%Lf %Lf %Lf\n", aij.x, aij.y, aij.z);
            acc[i] = add(acc[i], aij);
            acc[j] = add(acc[j], neg(aij));
        }
    }
    //Update velocity and positions
    for (int i = 0;i < n;i++) {
        vect v = add(planets[i].vel, scalar_mult(acc[i], dt));
        planets[i].pos = add(planets[i].pos, scalar_mult(v, dt)); // sf = si + v.dt
        planets[i].vel = v;
    }
}
