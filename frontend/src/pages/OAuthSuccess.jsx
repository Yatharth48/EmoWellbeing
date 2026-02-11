import React, { useEffect } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { apiRequest } from "../api";

export default function OAuthSuccess() {
  const [params] = useSearchParams();
  const navigate = useNavigate();
  const { login } = useAuth();

  useEffect(() => {
    const token = params.get("token");
    if (!token) {
      navigate("/login");
      return;
    }

    async function finishLogin() {
      try {
        localStorage.setItem("emowell_token", token);

        const user = await apiRequest("/api/auth/me");

        login(res.access_token, res.user);

        navigate("/chat");
      } catch (err) {
        console.error(err);
        navigate("/login");
      }
    }

    finishLogin();
  }, []);

  return <p>Signing you in…</p>;
}
