void newmark_beta(
    const double *force, const double *time, int n,
    double wn, double zeta, double m, double beta, double gamma_,
    double *disp, double *vel, double *accel
) {
    double k = m * wn * wn;
    double c = 2 * m * zeta * wn;

    // Initial conditions
    disp[0] = 0.0;
    vel[0] = 0.0;
    accel[0] = (force[0] - c * vel[0] - k * disp[0]) / m;

    double h = time[1] - time[0];
    double a1 = (1 / (beta * h * h)) * m + (gamma_ / (beta * h)) * c;
    double a2 = (1 / (beta * h)) * m + ((gamma_ / beta) - 1) * c;
    double a3 = ((1 / (2 * beta)) - 1) * m + h * (gamma_ / (2 * beta) - 1) * c;
    double ks = k + a1;

    for (int i = 0; i < n - 1; i++) {
        double ps = force[i + 1] + a1 * disp[i] + a2 * vel[i] + a3 * accel[i];
        disp[i + 1] = ps / ks;
        vel[i + 1] = (gamma_ / (beta * h)) * (disp[i + 1] - disp[i]) + (1 - gamma_ / beta) * vel[i] + h * (1 - gamma_ / (2 * beta)) * accel[i];
        accel[i + 1] = (1 / (beta * h * h)) * (disp[i + 1] - disp[i]) - (1 / (beta * h)) * vel[i] - ((1 / (2 * beta)) - 1) * accel[i];
    }
}