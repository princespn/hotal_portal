import { Link } from "react-router-dom";

const TopHeader = () => {
    return (
        <header className="border-bottom bg-white sticky-top">

            <nav className="navbar navbar-expand-lg">

                <div className="container">

                    <Link
                        to="/"
                        className="navbar-brand fw-bold"
                    >
                        <i className="bi bi-building text-primary me-2"></i>
                        Hotel<span className="text-primary">SaaS</span>
                    </Link>

                    <div className="ms-auto d-flex gap-2">

                        <button
                            type="button"
                            className="btn btn-outline-primary"
                            data-bs-toggle="modal"
                            data-bs-target="#loginModal"
                        >
                            Login
                        </button>

                        <button
                            type="button"
                            className="btn btn-primary"
                            data-bs-toggle="modal"
                            data-bs-target="#registrationModal"
                        >
                            Register
                        </button>

                    </div>

                </div>

            </nav>

        </header>
    );
};

export default TopHeader;