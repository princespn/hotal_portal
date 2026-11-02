import { useState } from "react";

const Login = () => {

    const [form, setForm] = useState({
        email: "",
        password: "",
    });

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        setError("");
        setLoading(true);

        try {
            // FastAPI login API will be connected here
            console.log(form);

        } catch (error) {
            setError(
                error.response?.data?.detail ||
                "Invalid email or password."
            );
        } finally {
            setLoading(false);
        }
    };

    return (
        <div
            className="modal fade"
            id="loginModal"
            tabIndex="-1"
            aria-hidden="true"
        >
            <div className="modal-dialog modal-dialog-centered">

                <div className="modal-content border-0 shadow">

                    <div className="modal-header">

                        <h5 className="modal-title fw-bold">
                            <i className="bi bi-box-arrow-in-right text-primary me-2"></i>
                            Login
                        </h5>

                        <button
                            type="button"
                            className="btn-close"
                            data-bs-dismiss="modal"
                        ></button>

                    </div>

                    <div className="modal-body p-4">

                        {error && (
                            <div className="alert alert-danger">
                                {error}
                            </div>
                        )}

                        <form onSubmit={handleSubmit}>

                            <div className="mb-3">

                                <label className="form-label">
                                    Email
                                </label>

                                <input
                                    type="email"
                                    name="email"
                                    value={form.email}
                                    onChange={handleChange}
                                    className="form-control"
                                    placeholder="Enter your email"
                                    required
                                />

                            </div>

                            <div className="mb-4">

                                <label className="form-label">
                                    Password
                                </label>

                                <input
                                    type="password"
                                    name="password"
                                    value={form.password}
                                    onChange={handleChange}
                                    className="form-control"
                                    placeholder="Enter your password"
                                    required
                                />

                            </div>

                            <button
                                type="submit"
                                className="btn btn-primary w-100"
                                disabled={loading}
                            >
                                {loading ? (
                                    <>
                                        <span className="spinner-border spinner-border-sm me-2"></span>
                                        Logging in...
                                    </>
                                ) : (
                                    "Login"
                                )}
                            </button>

                        </form>

                    </div>

                    <div className="modal-footer justify-content-center">

                        <small className="text-secondary">
                            Don't have an account?
                        </small>

                        <button
                            type="button"
                            className="btn btn-link btn-sm"
                            data-bs-dismiss="modal"
                            data-bs-toggle="modal"
                            data-bs-target="#registrationModal"
                        >
                            Register
                        </button>

                    </div>

                </div>

            </div>
        </div>
    );
};

export default Login;