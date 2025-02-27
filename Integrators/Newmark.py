import numpy as np

from Constants import g
from Integrators.GroundMotionIntegrator import groundMotionIntegrator


# from typing import Tuple


def newmarkBeta(applied_force: np.ndarray, t_arr: np.ndarray, wn: float, zeta: float, m=1, beta: float = 1 / 4,
                gamma_: float = 0.5) \
        -> [np.ndarray, np.ndarray, np.ndarray]:


    disp = np.zeros(len(t_arr))
    vel = np.zeros(len(t_arr))
    accel = np.zeros(len(t_arr))


    # ground_accel_arr=ground_accel_arr * m           #Check this line
    k = m * wn ** 2
    c = 2 *m* zeta * wn

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< In Progress >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # disp[0] = 0
    # vel[0] = 0
    # # accel[0] = (1/m)*ground_accel_arr[0]-c*vel[0]-k*disp[0]
    # accel[0] = (1/m) * (ground_accel_arr[0] - c * vel[0] - k * disp[0])
    #
    # wd = wn * np.sqrt(1 - zeta ** 2);
    #
    # # If timestep is constant
    # h = t_arr[1]-t_arr[0]
    #
    # ms = m + lambda_ *h*c + beta * h ** 2 * k;
    #
    # for i in range(0, len(t_arr) - 1):
    #     dps = -k * disp[i] - (c + h * k) * vel[i] - (h * (1 -lambda_) * c + ((h ** 2) / 2)
    #                                          * (1 - 2 * beta) * k) * accel[i] + ground_accel_arr[i + 1]
    #     accel[i + 1] = dps / ms
    #     vel[i + 1] = vel[i] + ((1 -lambda_) * accel[i] +lambda_ * accel[i+1])*h
    #     disp[i + 1] = disp[i] + vel[i] * h + ((1 - 2 * beta) * accel[i] + 2 * beta * accel[i + 1]) * (h ** 2) / 2
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< In Progress >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    disp = np.zeros(len(t_arr))
    vel = np.zeros(len(t_arr))
    accel = np.zeros(len(t_arr))  # Acceleration
    h = t_arr[1] - t_arr[0]

    disp[0] = 0
    vel[0] = 0
    # accel[0]=(1/m)*(ground_accel_arr[0]-c*vel[0]-k*disp[0])
    accel[0]=0

    ks = k + (3 * c / h) + (6*m / h ** 2)
    # print(ks)

    # for i in range(len(t_arr) - 2):
    #     print(accel[i-1])
    #     dps = (ground_accel_arr[i + 1] - ground_accel_arr[i]) + (6*m / h + 3 * c) * vel[i] + (3*m-c*h/2) * accel[i]
    #     # print(dps)
    #     del_disp = dps / ks
    #     # print(del_disp)
    #     # del_vel = (2 / h) * del_disp - 2 * vel[i]
    #     del_vel=(1/2)*(del_disp/(beta*h) -disp[i]/beta + (2-1/(2*beta))*accel[i]*h)
    #     # d1=(4 / h ** 2)
    #     # d2=(del_disp - vel[i]) * h
    #     # d3= 2 * accel[i]
    #     #
    #     # del_accel = d1* d2 - d3
    #     del_accel = (6 / h) * (del_disp/h - vel[i])  - 3 * accel[i]
    #
    #     disp[i + 1] = disp[i] + del_disp
    #     vel[i + 1] = vel[i] + del_vel
    #     accel[i + 1] = accel[i] + del_accel


    # for i in range(len(t_arr) - 2):
    #     dpi_ = ((applied_force[i + 1] - applied_force[i]) + (1 / (beta * h) + gamma_ / beta * 2 * zeta * wn) * vel[i] +
    #             (1 / (2 * beta) + h * (gamma_ / (2 * beta) - 1) * 2 * zeta * wn) * accel[i])
    #     ki_ = wn ** 2 + gamma_ / (beta * h) * 2 * zeta * wn + 1 / (beta * h ** 2)
    #
    #     del_disp = dpi_ / ki_
    #     disp[i+1]=del_disp+disp[i]
    #
    #     del_vel = gamma_ / (beta * h) * (disp[i+1] - disp[i]) - gamma_ / beta * vel[i] + h * (1 - gamma_ / (2 * beta)) * accel[i]
    #     vel[i + 1] = del_vel + vel[i]
    #
    #     del_accel = 1 / (beta * h ** 2) * (disp[i+1] - disp[i]) - 1 / (beta * h) * vel[i] - 1 / (2 * beta) * accel[i]
    #     accel[i + 1] = del_accel + accel[i]

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< In Progress >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # dt=h
    #
    # B = beta
    # G = gamma_
    # Z=zeta
    # W=wn
    #
    # a0 = 1 / (B * dt) + 2 * G * Z * W / B
    # a1 = 1 / (2 * B) + dt * G * Z * 2 * W / (2 * B) - dt * Z * 2 * W
    # a2 = G / (B * dt)
    # a3 = G / B
    # a4 = dt * (1 - G / (2 * B))
    # a5 = 1 / (B * dt * dt)
    # a6 = 1 / (B * dt)
    # a7 = 0.5 / B
    #
    # k_prime = W * W + 2 * G * Z * W / (B * dt) + 1 / (B * dt * dt)
    #
    # for i in range(len(t_arr) - 2):
    #     del_disp = (-applied_force[i] + applied_force[i - 1] + a0 * vel[i - 1] + a1 * accel[i - 1]) / k_prime
    #     del_vel = a2 * del_disp - a3 * vel[i - 1] + a4 * accel[i - 1]
    #     del_accel = a5 * del_disp - a6 * vel[i - 1] - a7 * accel[i - 1]
    #
    #     disp[i] = disp[i - 1] + del_disp
    #     vel[i] = vel[i - 1] + del_vel
    #     accel[i] = accel[i - 1] + del_accel


    # Trial 4
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< In Progress >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # accel = []
    # vel = []
    # disp = []
    # PSA = []
    #
    # vel_0 = 0
    # u0 = 0
    # P0 = 0
    # g = 9.81  # in/s^2
    # beta = beta
    # Gamma = gamma_
    # dt = t_arr[1] - t_arr[0]
    #
    # zeta = zeta  # damping ratio
    # m = 1  # Assume a generic mass
    # # wn = 2 * np.pi / T  # Compute natural circular frequency
    # wn=wn
    # k = m * wn * wn  # Compute stiffness corresponding to the given mass
    # c = 2 * zeta * wn * m  # Compute the damping coefficient
    #
    # accel.append((P0 - c * vel_0 - k * u0) / m)
    # vel.append(0)
    # disp.append(0)
    # PSA.append(disp[0] * wn * wn)
    # a1 = 1 / (beta * dt ** 2) * m + Gamma / (beta * dt) * c
    # a2 = 1 / (beta * dt) * m + (Gamma / beta - 1) * c
    # a3 = (1 / (2 * beta) - 1) * m + dt * (Gamma / 2 * beta - 1) * c
    # k_hat = k + a1
    # p_hat = []
    # p_hat.append(0)
    #
    # acceleration=applied_force/m
    #
    # for i in range(len(acceleration) - 1):
    #     p_hat_fut = (acceleration[i + 1]/g) * m + a1 * disp[i] + a2 * vel[i] + a3 * accel[i]
    #     # p_hat_fut = accel[i+1]
    #     p_hat.append(p_hat_fut)
    #     disp_fut = p_hat_fut / k_hat
    #     veloc_fut = Gamma / (beta * dt) * (disp_fut - disp[i]) + (1 - Gamma / beta) * vel[i] + dt * (
    #                 1 - (Gamma / (2 * beta))) * accel[i]
    #     accel_fut = (1 / (beta * dt ** 2) * (disp_fut - disp[i])) - 1 / (beta * dt) * vel[i] - (
    #                 1 / (2 * beta) - 1) * accel[i]
    #     disp.append(disp_fut)
    #     vel.append(veloc_fut)
    #     accel.append(accel_fut)
    #     PSA.append(disp_fut * wn * wn / g)
    #
    # disp=np.array(disp)
    # vel = np.array(vel)
    # accel = np.array(accel)

    # Trial 5
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< In Progress >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    accel[0]=(applied_force[0]-c*vel[0]- k*disp[0])/m
    h=t_arr[1]-t_arr[0]

    a1=(1/(beta*h**2))*m + (gamma_ /(beta*h))*(c)
    a2=(1/(beta*h))*m + ((gamma_ /beta) -1)*(c)
    a3 = ((1 / (2 * beta)) - 1)*m + (h) * (gamma_ / (2 * beta) - 1) * (c)

    ks=k+a1

    for i in range(len(applied_force) - 1):

        ps=applied_force[i+1] + a1*disp[i] + a2*vel[i]+ a3 *accel[i]
        disp[i+1]=ps/ks
        vel[i+1]= (gamma_ /(beta*h))*(disp[i+1] - disp[i]) + (1- gamma_/beta)*vel[i] + h* (1- gamma_ /(2*beta))*accel[i]
        accel[i+1]= (1/(beta* h**2))*(disp[i+1] - disp[i]) - (1/(beta*h))*vel[i]- ((1/(2*beta)) -1)* accel[i]


    return disp, vel, accel

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< In Progress >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



    return disp, vel, accel


def newmarkBeta_GroundMotion(ground_accel_arr: np.ndarray, t_arr: np.ndarray, wn: float, zeta: float, m=1, beta: float = 1 / 6,
                gamma_: float = 0.5, g_units=False) \
        -> [np.ndarray, np.ndarray, np.ndarray]:

    # TODO handle g here
    # disp_ground, vel_ground, accel_ground, time = groundMotionIntegrator([t_arr, ground_accel_arr], g_units=g_units)

    if g_units:
        accel_ground=ground_accel_arr*g
    else:
        accel_ground=ground_accel_arr

    eq_force= -accel_ground*m


    disp, vel, accel = newmarkBeta(eq_force, t_arr, wn=wn, zeta= zeta, m=m, beta=beta, gamma_=gamma_ )

    # disp_r=disp-disp_ground
    # vel_r=vel-vel_ground


    return disp, vel, accel