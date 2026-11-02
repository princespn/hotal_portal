import { useState } from "react";

const Registration = () => {

    const [form, setForm] = useState({
        name: "",
        email: "",
        phone: "",
        password: "",
        password_confirmation: "",
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

        if (form.password !== form.password_confirmation) {
            setError("Passwords do not match.");
            return;
        }

        setLoading(true);

        try {
            // FastAPI registration API will be connected here
            console.log(form);

        } catch (error) {
            setError(
                error.response?.data?.detail ||
                "Registration failed."
            );
        } finally {
            setLoading(false);
        }
    };

    return (
        <div
            className="modal fade"
            id="registrationModal"
            tabIndex="-1"
            aria-hidden="true"
        >
            <div className="modal-dialog modal-dialog-centered">

                <div className="modal-content border-0 shadow">

                    <div className="modal-header">

                        <h5 className="modal-title fw-bold">
                            <i className="bi bi-person-plus text-primary me-2"></i>
                            Create Account
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
                                    Full Name
                                </label>

                                <input
                                    type="text"
                                    name="name"
                                    value={form.name}
                                    onChange={handleChange}
                                    className="form-control"
                                    placeholder="Enter your name"
                                    required
                                />

                            </div>

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

                            <div className="mb-3">

                                <label className="form-label">
                                    Phone
                                </label>

                                <input
                                    type="tel"
                                    name="phone"
                                    value={form.phone}
                                    onChange={handleChange}
                                    className="form-control"
                                    placeholder="Enter your phone"
                                />

                            </div>

                            <div className="mb-3">

                                <label className="form-label">
                                    Password
                                </label>

                                <input
                                    type="password"
                                    name="password"
                                    value={form.password}
                                    onChange={handleChange}
                                    className="form-control"
                                    placeholder="Minimum 8 characters"
                                    minLength="8"
                                    required
                                />

                            </div>

                            <div className="mb-4">

                                <label className="form-label">
                                    Confirm Password
                                </label>

                                <input
                                    type="password"
                                    name="password_confirmation"
                                    value={form.password_confirmation}
                                    onChange={handleChange}
                                    className="form-control"
                                    placeholder="Confirm password"
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
                                        Creating Account...
                                    </>
                                ) : (
                                    "Create Account"
                                )}
                            </button>

                        </form>

                    </div>

                    <div className="modal-footer justify-content-center">

                        <small className="text-secondary">
                            Already have an account?
                        </small>

                        <button
                            type="button"
                            className="btn btn-link btn-sm"
                            data-bs-dismiss="modal"
                            data-bs-toggle="modal"
                            data-bs-target="#loginModal"
                        >
                            Login
                        </button>

                    </div>

                </div>

            </div>
        </div>
    );
};

export default Registration;