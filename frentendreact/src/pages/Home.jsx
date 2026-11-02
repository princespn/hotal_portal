import Login from "../components/Login";
import Registration from "../components/Registration";

const Home = () => {
    return (
        <>
            <section className="py-5 bg-light">
                <div className="container py-5">
                    <div className="row align-items-center">

                        <div className="col-lg-7">

                            <span className="badge bg-primary-subtle text-primary mb-3 px-3 py-2">
                                Modern Hotel Management Platform
                            </span>

                            <h1 className="display-4 fw-bold mb-4">
                                Manage Your Hotel{" "}
                                <span className="text-primary">
                                    Smarter
                                </span>
                            </h1>

                            <p className="lead text-secondary mb-4">
                                Manage rooms, guests, bookings, payments
                                and hotel operations from one platform.
                            </p>

                            <button
                                className="btn btn-primary btn-lg px-4"
                                data-bs-toggle="modal"
                                data-bs-target="#registrationModal"
                            >
                                Get Started
                                <i className="bi bi-arrow-right ms-2"></i>
                            </button>

                        </div>

                    </div>
                </div>
            </section>

            {/* Login Component */}
            <Login />

            {/* Registration Component */}
            <Registration />
        </>
    );
};

export default Home;