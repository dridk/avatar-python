# API Version 0.4.14
# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2022-12-01T11:24:50+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field, constr


class AnalysisStatus(Enum):
    """
    An enumeration.
    """

    started = "started"
    done = "done"


class ClusterStats(BaseModel):
    n_active_tasks: Optional[int] = Field(None, title="N Active Tasks")
    available_concurrency: Optional[int] = Field(None, title="Available Concurrency")
    utilization_rate_100: Optional[int] = Field(None, title="Utilization Rate 100")
    status_message: Optional[str] = Field("", title="Status Message")


class ColumnStats(BaseModel):
    label: str = Field(..., title="Label")
    dtype: str = Field(..., title="Dtype")
    missing_number: int = Field(..., title="Missing Number")
    missing_proportion: float = Field(..., title="Missing Proportion")
    unique_number: int = Field(..., title="Unique Number")
    unique_proportion: float = Field(..., title="Unique Proportion")
    mean: Optional[float] = Field(None, title="Mean")
    median: Optional[float] = Field(None, title="Median")
    standard_deviation: Optional[float] = Field(None, title="Standard Deviation")
    mode: Optional[Union[str, int, float]] = Field(None, title="Mode")
    is_skewed: Optional[bool] = Field(None, title="Is Skewed")
    is_rare: Optional[bool] = Field(None, title="Is Rare")


class ColumnType(Enum):
    """
    An enumeration.
    """

    int = "int"
    bool = "bool"
    category = "category"
    float = "float"
    datetime = "datetime"


class DatasetSummary(BaseModel):
    stats: List[ColumnStats] = Field(..., title="Stats")


class ExplainedVariance(BaseModel):
    raw: List[float] = Field(..., title="Raw")
    ratio: List[float] = Field(..., title="Ratio")


class ForgottenPasswordRequest(BaseModel):
    email: str = Field(..., title="Email")


class ImputeMethod(Enum):
    """
    An enumeration.
    """

    knn = "knn"
    mode = "mode"
    median = "median"
    mean = "mean"
    fast_knn = "fast_knn"


class JobKind(Enum):
    """
    An enumeration.
    """

    avatarization = "avatarization"
    privacy_metrics = "privacy_metrics"
    signal_metrics = "signal_metrics"


class JobProgress(BaseModel):
    completion_rate_100: int = Field(..., title="Completion Rate 100")
    name: Optional[str] = Field(None, title="Name")
    created_at: datetime = Field(..., title="Created At")


class JobStatus(Enum):
    """
    An enumeration.
    """

    pending = "pending"
    started = "started"
    success = "success"
    failure = "failure"
    unknown = "unknown"


class LoginResponse(BaseModel):
    access_token: str = Field(..., title="Access Token")
    token_type: str = Field(..., title="Token Type")


class PrivacyMetrics(BaseModel):
    hidden_rate: float = Field(..., title="Hidden Rate")
    local_cloaking: float = Field(..., title="Local Cloaking")
    distance_to_closest: float = Field(..., title="Distance To Closest")
    closest_distances_ratio: float = Field(..., title="Closest Distances Ratio")


class Projections(BaseModel):
    records: List[List[float]] = Field(..., title="Records")
    avatars: List[List[float]] = Field(..., title="Avatars")


class Report(BaseModel):
    id: UUID = Field(..., title="Id")
    user_id: UUID = Field(..., title="User Id")
    job_id: UUID = Field(..., title="Job Id")
    created_at: Optional[datetime] = Field(None, title="Created At")
    download_url: str = Field(..., title="Download Url")


class ReportCreate(BaseModel):
    job_id: UUID = Field(..., title="Job Id")


class ResetPasswordRequest(BaseModel):
    email: str = Field(..., title="Email")
    new_password: constr(min_length=12) = Field(..., title="New Password")
    new_password_repeated: constr(min_length=12) = Field(
        ..., title="New Password Repeated"
    )
    token: UUID = Field(..., title="Token")


class SignalMetrics(BaseModel):
    hellinger_mean: float = Field(..., title="Hellinger Mean")
    hellinger_std: float = Field(..., title="Hellinger Std")
    correlation_difference_ratio: Optional[float] = Field(
        None, title="Correlation Difference Ratio"
    )


class SignalMetricsParameters(BaseModel):
    original_id: UUID = Field(..., title="Original Id")
    seed: Optional[int] = Field(None, title="Seed")
    job_id: Optional[UUID] = Field(None, title="Job Id")
    avatars_id: UUID = Field(..., title="Avatars Id")


class UserRole(Enum):
    """
    An enumeration.
    """

    admin = "admin"
    user = "user"


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")


class Login(BaseModel):
    grant_type: Optional[constr(regex=r"password")] = Field(None, title="Grant Type")
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    scope: Optional[str] = Field("", title="Scope")
    client_id: Optional[str] = Field(None, title="Client Id")
    client_secret: Optional[str] = Field(None, title="Client Secret")


class CreateDataset(BaseModel):
    file: bytes = Field(..., title="File")


class ColumnDetail(BaseModel):
    type: ColumnType
    label: str = Field(..., title="Label")


class CreateUser(BaseModel):
    username: Optional[str] = Field(None, title="Username")
    email: Optional[str] = Field(None, title="Email")
    role: Optional[UserRole] = "user"
    is_email_confirmed: Optional[bool] = Field(False, title="Is Email Confirmed")
    password: Optional[constr(min_length=12)] = Field(None, title="Password")


class Dataset(BaseModel):
    id: UUID = Field(..., title="Id")
    hash: str = Field(..., title="Hash")
    name: Optional[str] = Field(None, title="Name")
    columns: Optional[List[ColumnDetail]] = Field(None, title="Columns")
    download_url: str = Field(..., title="Download Url")
    analysis_status: Optional[AnalysisStatus] = None
    analysis_duration: Optional[float] = Field(None, title="Analysis Duration")
    nb_lines: Optional[int] = Field(None, title="Nb Lines")
    summary: Optional[DatasetSummary] = None


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title="Detail")


class ImputationParameters(BaseModel):
    method: Optional[ImputeMethod] = None
    k: Optional[int] = Field(None, title="K")
    training_fraction: Optional[float] = Field(None, title="Training Fraction")


class PrivacyMetricsParameters(BaseModel):
    original_id: UUID = Field(..., title="Original Id")
    seed: Optional[int] = Field(None, title="Seed")
    job_id: Optional[UUID] = Field(None, title="Job Id")
    unshuffled_avatars_id: UUID = Field(..., title="Unshuffled Avatars Id")
    imputation: Optional[ImputationParameters] = None
    ncp: Optional[int] = Field(None, title="Ncp")


class SignalMetricsJob(BaseModel):
    id: UUID = Field(..., title="Id")
    status: JobStatus
    dataset_id: Optional[UUID] = Field(
        None,
        description="Deprecated, use parameters.dataset_id instead.",
        title="Dataset Id",
    )
    error_message: Optional[str] = Field(None, title="Error Message")
    traceback: Optional[str] = Field(None, title="Traceback")
    result: Optional[SignalMetrics] = None
    parameters: SignalMetricsParameters
    current_progress: Optional[JobProgress] = None


class SignalMetricsJobCreate(BaseModel):
    kind: Optional[JobKind] = "signal_metrics"
    parameters: SignalMetricsParameters


class PatchDataset(BaseModel):
    columns: List[ColumnDetail] = Field(..., title="Columns")


class AvatarizationParameters(BaseModel):
    k: int = Field(..., title="K")
    dataset_id: Optional[UUID] = Field(
        None,
        description="The 'Optional' type is here for Backward Compatibility reasons",
        title="Dataset Id",
    )
    column_weights: Optional[Dict[str, float]] = Field(None, title="Column Weights")
    ncp: Optional[int] = Field(None, title="Ncp")
    seed: Optional[int] = Field(None, title="Seed")
    imputation: Optional[ImputationParameters] = None
    to_categorical_threshold: Optional[int] = Field(
        None, title="To Categorical Threshold"
    )


class AvatarizationResult(BaseModel):
    privacy_metrics: PrivacyMetrics
    signal_metrics: SignalMetrics
    avatars_dataset: Dataset
    sensitive_unshuffled_avatars_datasets: Dataset


class PrivacyMetricsJob(BaseModel):
    id: UUID = Field(..., title="Id")
    status: JobStatus
    dataset_id: Optional[UUID] = Field(
        None,
        description="Deprecated, use parameters.dataset_id instead.",
        title="Dataset Id",
    )
    error_message: Optional[str] = Field(None, title="Error Message")
    traceback: Optional[str] = Field(None, title="Traceback")
    result: Optional[PrivacyMetrics] = None
    parameters: PrivacyMetricsParameters
    current_progress: Optional[JobProgress] = None


class PrivacyMetricsJobCreate(BaseModel):
    kind: Optional[JobKind] = "privacy_metrics"
    parameters: PrivacyMetricsParameters


class AvatarizationJob(BaseModel):
    id: UUID = Field(..., title="Id")
    status: JobStatus
    dataset_id: Optional[UUID] = Field(
        None,
        description="Deprecated, use parameters.dataset_id instead.",
        title="Dataset Id",
    )
    error_message: Optional[str] = Field(None, title="Error Message")
    traceback: Optional[str] = Field(None, title="Traceback")
    result: Optional[AvatarizationResult] = None
    parameters: AvatarizationParameters
    current_progress: Optional[JobProgress] = None


class AvatarizationJobCreate(BaseModel):
    kind: Optional[JobKind] = "avatarization"
    parameters: AvatarizationParameters
