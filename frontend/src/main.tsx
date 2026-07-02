import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import {
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query";

import "./index.css";

import SignupPage from "./pages/SignupPage";
import CreateProjectPage from "./pages/CreateProjectPage";
import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import DecisionPage from "./pages/DecisionPage";
import ProtectedRoute from "./components/ProtectedRoute";

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/signup" element={<SignupPage />} />
          <Route
  path="/create-project"
  element={
    <ProtectedRoute>
      <CreateProjectPage />
    </ProtectedRoute>
  }
/>
          {/* Login */}
          <Route path="/" element={<LoginPage />} />

          {/* Dashboard */}
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <DashboardPage />
              </ProtectedRoute>
            }
          />
<Route
  path="/projects/new"
  element={
    <ProtectedRoute>
      <CreateProjectPage />
    </ProtectedRoute>
  }
/>
          {/* Decision Page */}
          <Route
            path="/decisions/result"
            element={
              <ProtectedRoute>
                <DecisionPage />
              </ProtectedRoute>
            }
          />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  </React.StrictMode>
);