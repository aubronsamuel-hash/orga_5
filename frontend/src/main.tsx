import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import Planning from "./pages/Planning";
import { isAuthenticated } from "./lib/auth";
import "./styles.css";

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/planning"
          element={isAuthenticated() ? <Planning /> : <Navigate to="/login" replace />}
        />
        <Route path="*" element={<Navigate to="/planning" replace />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
