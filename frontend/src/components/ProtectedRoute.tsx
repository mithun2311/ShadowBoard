import { Navigate } from "react-router-dom";
import { useAuth } from "../store/auth";

interface Props {
  children: React.ReactNode;
}

export default function ProtectedRoute({ children }: Props) {
  const token = useAuth((state) => state.token);

  if (!token) {
    return <Navigate to="/" replace />;
  }

  return <>{children}</>;
}